from locators.locators import MainPageLocators
from functions import get_element

class MainPage:
	def __init__(self, driver, wait):
		self.driver = driver
		self.wait = wait
		self.driver.get('https://tjournal.ru')
		self.locators = MainPageLocators()

	def click_login_button(self):
		element = get_element(self, self.locators.LOGIN_BUTTON)
		element.click()

	def check_login_form_exist(self):
		element = get_element(self, self.locators.LOGIN_FORM)
		return element is not None

	def check_news_banner_exit(self):
		element = get_element(self, self.locators.NEWS_BANNER)
		return element is not None

	def check_sponsors_notes_exist(self):
		element = get_element(self, self.locators.SPONSORS_NOTES)
		return element is not None

	def click_agreement_link(self):
		element = get_element(self, self.locators.AGREEMENT_LINK)
		element.click()

	def click_raiting_button(self):
		element = get_element(self, self.locators.RATING_BUTTON)
		element.click()

	def click_about_button(self):
		element = get_element(self, self.locators.ABOUT_BUTTON)
		element.click()

	def click_configure_button(self):
		element = get_element(self, self.locators.CONFIGURE_BUTTON)
		element.click()

	def click_login_by_vk(self):
		element = get_element(self, self.locators.LOGIN_BY_VK)
		element.click()

	def click_profile_triangle(self):
		element = get_element(self, self.locators.PROFILE_TRIANGLE)
		element.click()

	def click_logout_button(self):
		element = get_element(self, self.locators.LOGOUT_BUTTON)
		element.click()
