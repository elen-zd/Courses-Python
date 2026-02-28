from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        self._driver = driver

    def calc_page(self):
        WebDriverWait(self._driver, 10)
        self._driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    def field_delay(self):
        field_del = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#delay"))
        )
        field_del.clear()
        field_del.send_keys("45")

    def buttons(self):
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[1]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[4]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[2]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[15]").click()

    def results(self):
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//*[@id='calculator']/div[1]/div"), "15")
        )
        result = self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[1]/div")
        return result.text
