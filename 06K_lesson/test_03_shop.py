import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(browser):
    wait_fox = WebDriverWait(browser, 10)
    browser.implicitly_wait(4)
    browser.get("https://www.saucedemo.com/")

    password = "secret_sauce"

    login_user = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#user-name"))
    )
    login_user.clear()
    login_user.send_keys("standard_user")

    password_user = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#password")
        )
    )
    password_user.clear()
    password_user.send_keys(password)

    button_login = wait_fox.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#login-button")
        )
    )
    button_login.click()

    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
    ).click()

    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

    browser.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
    ).click()

    browser.find_element(
        By.CSS_SELECTOR, "a[data-test=shopping-cart-link]"
    ).click()

    button_checkout = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#checkout")
        )
    )
    button_checkout.click()

    first_name = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#first-name")
        )
    )
    first_name.clear()
    first_name.send_keys("Алена")

    last_name = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#last-name")
        )
    )
    last_name.clear()
    last_name.send_keys("Зубина")

    zip_code = wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#postal-code")
        )
    )
    zip_code.clear()
    zip_code.send_keys("123456")

    browser.find_element(By.CSS_SELECTOR, "#continue").click()

    wait_fox.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[data-test=total-label")
        )
    )
    price_total = browser.find_element(
        By.CSS_SELECTOR, "div[data-test=total-label").text
    assert price_total == "Total: $58.29"
    print(price_total)
