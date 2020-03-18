from pages.main_page import MainPage


def test_basic_elements(browser_is_opened):
    main_page = MainPage(*browser_is_opened)
    assert main_page.check_news_banner_exit()
    assert main_page.check_sponsors_notes_exist()
