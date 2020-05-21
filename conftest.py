import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.vk_login_page import VKLoginPage
from functions import get_mail_logpass


@pytest.fixture
def browser_is_opened():
	driver = webdriver.Chrome()
	wait = WebDriverWait(driver, 15)
	yield driver, wait
	driver.close()


@pytest.fixture
def user_is_logined(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_login_button()
	main_page.click_login_by_mail()

	mail, password = get_mail_logpass()
	main_page.write_mail(mail)
	main_page.write_pass(password)
	main_page.finish_login_by_mail()
	yield browser_is_opened

	main_page.click_profile_triangle()
	main_page.click_logout_button()
