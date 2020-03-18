from pages.main_page import MainPage
from pages.simple_pages import AgreementPage


def test_agreement(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_login_button()
	main_page.click_agreement_link()
	agreement_page = AgreementPage(*browser_is_opened)
	agreement_page.check_title()
