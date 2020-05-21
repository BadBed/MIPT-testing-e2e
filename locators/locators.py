from selenium.webdriver.common.by import By


class MainPageLocators:
	def __init__(self):
		self.SEARCH_INPUT = (
			By.CLASS_NAME, 
			'search__input')
		self.LOGIN_BUTTON = (
			By.CLASS_NAME,
			'main_menu__auth__login')
		self.LOGIN_FORM = (
			By.CLASS_NAME,
			'auth-form__main')
		self.NEWS_BANNER = (
			By.CLASS_NAME,
			'content-feed__link')
		self.SPONSORS_NOTES = (
			By.CLASS_NAME,
			'sidebar__footer__container')
		self.AGREEMENT_LINK = (
			By.LINK_TEXT,
			'согласие на обработку персональных данных')
		self.RATING_BUTTON = (
			By.PARTIAL_LINK_TEXT,
			'Рейтинг TJ')
		self.ABOUT_BUTTON = (
			By.PARTIAL_LINK_TEXT,
			'Реклама и контакты')
		self.CONFIGURE_BUTTON = (
			By.CLASS_NAME,
			'subsites_tune_widget__button')
		self.LOGIN_BY_VK = (
			By.XPATH,
			'//*[@class="social-auth__button"]')
		self.PROFILE_TRIANGLE = (
			By.CLASS_NAME,
			'possession_triangle')
		self.LOGOUT_BUTTON = (
			By.PARTIAL_LINK_TEXT,
			'Выход')
		self.LOGIN_BY_MAIL = (
			By.PARTIAL_LINK_TEXT,
			'Через почту')
		self.MAIL_INPUT = (
			By.XPATH,
			'//input[@type="email"]')
		self.PASS_INPUT = (
			By.XPATH,
			'//input[@type="password"]')
		self.SEND_MAILPASS_BUTTON = (
			By.XPATH,
			'//input[@type="submit"]')


class VKLoginPageLocators:
	def __init__(self):
		self.LOGIN_INPUT = (
			By.XPATH,
			'//input[@name="email"]')
		self.PASSWORD_INPUT = (
			By.XPATH,
			'//input[@name="pass"]')
		self.LOGIN_BUTTON = (
			By.CLASS_NAME,
			'oauth_button')
