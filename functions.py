from selenium.webdriver.support import expected_conditions


def get_element(page, locator):
	return page.wait.until(
		expected_conditions.presence_of_element_located(locator))
