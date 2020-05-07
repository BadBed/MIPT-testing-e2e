from pages.main_page import MainPage


def test_login_form(browser_is_opened):
	main_page = MainPage(*browser_is_opened)
	main_page.click_login_button()
	assert main_page.check_login_form_exist()

# Проверяет что мы можем корректно логиниться / разлогиниться.
def test_login_logout(user_is_logined):
	pass
