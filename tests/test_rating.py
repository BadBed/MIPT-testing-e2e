from pages.main_page import MainPage
from pages.simple_pages import RatingPage

def test_rating(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_raiting_button()
	rating_page = RatingPage(*browser_is_opened)
	rating_page.check_title()
