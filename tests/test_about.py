from pages.main_page import MainPage
from pages.simple_pages import AboutPage

def test_about(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_about_button()
	about_page = AboutPage(*browser_is_opened)
	about_page.check_title()
