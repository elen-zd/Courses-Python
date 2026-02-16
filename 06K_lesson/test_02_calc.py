import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(browser):
    wait = WebDriverWait(browser, 45)
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    field_delay = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#delay"))
    )
    field_delay.clear()
    field_delay.send_keys("45")

    browser.find_element(
        By.XPATH, "//*[@id='calculator']/div[2]/span[1]").click()
    browser.find_element(
        By.XPATH, "//*[@id='calculator']/div[2]/span[4]").click()
    browser.find_element(
        By.XPATH, "//*[@id='calculator']/div[2]/span[2]").click()
    browser.find_element(
        By.XPATH, "//*[@id='calculator']/div[2]/span[15]").click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//*[@id='calculator']/div[1]/div"), "15")
    )
    result = browser.find_element(
        By.XPATH, "//*[@id='calculator']/div[1]/div").text
    assert result == "15"
    print(result)
