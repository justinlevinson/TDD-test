from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from lists.models import Item

import sys

class NewVisitorTest(StaticLiveServerTestCase):
	
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url
		
	@classmethod	
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()
			
	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.implicitly_wait()
	
	def tearDown(self):
		self.browser.quit()
	


	#---------------------------------------------
	#  helper methods
	#---------------------------------------------

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
	



	#---------------------------------------------
	#  tests
	#---------------------------------------------


	#---------------------
	#  start and retrieve
	#---------------------

	def test_can_start_a_list_and_retrieve_it_later(self):
		#User goes to homepage
		self.browser.get(self.server_url)
		
		#Sees to-do in the title and header
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		#Invited to enter a to-do item on the homepage
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

		#User types "Buy feathers" into a text box
		inputbox.send_keys('Buy peacock feathers')

		#Page updates on enter and lists "1: Buy Feathers" as an item in the list
		inputbox.send_keys(Keys.ENTER)

		self.check_for_row_in_list_table('1: Buy peacock feathers')
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')

		#There is still a text box inviting an additional item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
	
		#User enters "Use feathers"
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		

		#Page updates again and shows both
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

		#a new user visits the site (remove browser to clear cookies)
		self.browser.quit()
		self.browser = webdriver.Firefox()
		
		self.browser.get(self.server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)
		
		#the new user starts a new list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)
		
		#the new user gets his own URN
		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)
		
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)
		
		#User sees the site has generated a unique URL with some explanatory text
		self.fail('to-finish')

		#User visits URL and sees to-do list is still there
		
	#---------------------
	#  start and retrieve
	#---------------------
		
	def test_layout_and_styling(self):
		self.browser.get(self.server_url)
		self.browser.set_window_size(1024,768)
		
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 512, delta=5)
		
		inputbox.send_keys('testing\n')
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2, 512, delta=5)




