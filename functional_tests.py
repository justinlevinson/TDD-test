from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from lists.models import Item

class NewVisitorTest(unittest.TestCase):
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
		self.browser.get('http://localhost:8000')
		
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

		self.check_for_row_in_list_table('1:Buy peacock feathers')

		#There is still a text box inviting an additional item
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
	
		#User enters "Use feathers"
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		

		#Page updates again and shows both
		self.check_for_row_in_list_table('1:Buy peacock feathers')
		self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')


		#User sees the site has generated a unique URL with some explanatory text
		self.fail('to-finish')

		#User visits URL and sees to-do list is still there
		


if __name__ == '__main__':
	unittest.main(warnings='ignore')




