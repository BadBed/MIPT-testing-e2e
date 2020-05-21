from locators.locators import VKLoginPageLocators
from functions import get_element
from selenium.webdriver.common.keys import Keys


class VKLoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.locators = VKLoginPageLocators()

    def click_login_button(self):
        element = get_element(self, self.locators.LOGIN_BUTTON, True)
        element.click()

    def write_in_login(self, text):
        element = get_element(self, self.locators.LOGIN_INPUT, True)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def write_in_password(self, text):
        element = get_element(self, self.locators.PASSWORD_INPUT, True)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)
