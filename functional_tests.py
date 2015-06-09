from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		#self.browser.implicitly_wait()
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		#User goes to homepage
		self.browser.get('http://localhost:8000')
		
		#Sees to-do in the title
		self.assertIn('To-Do', self.browser.title)

		#Invited to enter a to-do item on the homepage

		#User types "Buy feathers" into a text box

		#Page updates on enter and lists "1: Buy Feathers" as an item in the list

		#There is still a text box inviting an additional item

		#User enters "Use feathers"

		#Page updates again and shows both

		#User sees the site has generated a unique URL with some explanatory text

		#User visits URL and sees to-do list is still there

if __name__ == '__main__':
	unittest.main(warnings='ignore')




