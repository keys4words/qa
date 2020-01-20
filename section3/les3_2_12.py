import unittest, time
from selenium import webdriver

class Test2Pages(unittest.TestCase):
		
	def test_reg_form1(self):
		link = "http://suninjuly.github.io/registration1.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_class_name("first_block.first")
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_class_name("first_block.second")
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_class_name("first_block.third")
		input3.send_keys("test@test.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test registration1 failed!")

	def test_reg_form2(self):
		link = "http://suninjuly.github.io/registration2.html"
		browser = webdriver.Chrome()
		browser.get(link)
		input1 = browser.find_element_by_class_name("form-control.first")
		input1.send_keys("Ivan")
		input2 = browser.find_element_by_class_name("form-control.second")
		input2.send_keys("Petrov")
		input3 = browser.find_element_by_class_name("form-control.third")
		input3.send_keys("test@test.ru")
		button = browser.find_element_by_css_selector("button.btn")
		button.click()
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Test registration1 failed!")


if __name__ == "__main__":
    unittest.main()

