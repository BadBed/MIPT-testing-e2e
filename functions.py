from selenium.webdriver.support import expected_conditions


def get_element(page, locator, expect_visible=False):
    if expect_visible:
        return page.wait.until(
            expected_conditions.visibility_of_element_located(locator))
    else:
        return page.wait.until(
            expected_conditions.presence_of_element_located(locator))


def get_vk_logpass():
    with open('data/vk_login_password.txt') as f:
        return f.read().splitlines()


def get_mail_logpass():
    with open('data/mail_login_password.txt') as f:
        return f.read().splitlines()
