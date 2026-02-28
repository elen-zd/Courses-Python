from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddProduct:
    def __init__(self, driver):
        self._driver = driver

    def page_products(self):
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/inventory.html")

    def add_products(self):
        backpack = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            )
        )
        backpack.click()

        t_shirt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
            )
        )
        t_shirt.click()

        onesie = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
            )
        )
        onesie.click()

    def basket_enter(self):
        basket = self._driver.find_element(
            By.CSS_SELECTOR, "a[data-test=shopping-cart-link]"
        )
        basket.click()
