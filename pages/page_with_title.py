from selenium.webdriver.support import expected_conditions
from functions import get_element
from selenium.webdriver.common.by import By


class PageWithTitle:
	def __init__(self, driver, wait, title, title_class):
		self.driver = driver
		self.wait = wait
		self.title = title
		self.title_class = title_class

	def check_title(self):
		self.wait.until(expected_conditions.text_to_be_present_in_element(
			(By.CLASS_NAME, self.title_class), 
			self.title))
		

def create_page_class(title, title_class):
	def page(driver, wait):
		return PageWithTitle(driver, wait, title, title_class)
	return page
