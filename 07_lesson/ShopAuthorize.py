from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authorization:
    def __init__(self, driver):
        self._driver = driver

    def get_page_shop(self):
        WebDriverWait(self._driver, 10)
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/")

    def login_user(self):
        log_user = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#user-name"))
        )
        log_user.clear()
        log_user.send_keys("standard_user")

    def password_user(self):
        password = "secret_sauce"
        pass_user = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#password")
            )
        )
        pass_user.clear()
        pass_user.send_keys(password)

    def button(self):
        button_login = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#login-button")
            )
        )
        button_login.click()
