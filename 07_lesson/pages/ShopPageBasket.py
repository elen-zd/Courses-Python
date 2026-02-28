from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBasket:

    def __init__(self, driver):
        self._driver = driver

    def check_basket(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

        items = self._driver.find_elements(
                By.CSS_SELECTOR, "div[data-test=inventory-item]"
            )
        return len(items)

    def button_checkout(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#checkout")
            )
        )
        button.click()
