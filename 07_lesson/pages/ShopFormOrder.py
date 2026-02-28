from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormOrder:

    def __init__(self, driver):
        self._driver = driver

    def page_form_order(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def fill_form_order(self):
        first_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#first-name")
            )
        )
        first_name.clear()
        first_name.send_keys("Алена")

        last_name = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#last-name")
            )
        )
        last_name.clear()
        last_name.send_keys("Зубина")

        zip_code = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#postal-code")
            )
        )
        zip_code.clear()
        zip_code.send_keys("123456")

        button_continue = self._driver.find_element(
            By.CSS_SELECTOR, "#continue")
        button_continue.click()

    def page_price_order(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def get_price_order(self):
        price_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-test=total-label]")
            )
        )
        price_total = price_element.text.strip()
        return price_total
