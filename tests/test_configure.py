from pages.main_page import MainPage
from pages.simple_pages import ConfigurePage

def test_configure(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_configure_button()
	configure_page = ConfigurePage(*browser_is_opened)
	configure_page.check_title()
