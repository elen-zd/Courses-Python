import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form(browser):
    wait_browser = WebDriverWait(browser, 10)
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=first-name]"))
    )
    first_name.clear()
    first_name.send_keys("Иван")

    last_name = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=last-name]"))
    )
    last_name.clear()
    last_name.send_keys("Петров")

    address = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=address]"))
    )
    address.clear()
    address.send_keys("Ленина, 55-3")

    email = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=e-mail]"))
    )
    email.clear()
    email.send_keys("test@skypro.com")

    p_number = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=phone]"))
    )
    p_number.clear()
    p_number.send_keys("+7985899998787")

    zip_c = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=zip-code]"))
    )
    zip_c.clear()

    city = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=city]"))
    )
    city.clear()
    city.send_keys("Москва")

    country = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=country]"))
    )
    country.clear()
    country.send_keys("Россия")

    job_p = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=job-position]"))
    )
    job_p.clear()
    job_p.send_keys("QA")

    company = wait_browser.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[name=company]"))
    )
    company.clear()
    company.send_keys("SkyPro")

    button = wait_browser.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[type=submit]"))
    )
    button.click()

    wait_browser.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".alert"))
    )

    color_z_code = browser.find_element(
        By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert "alert py-2 alert-danger" in color_z_code
    print(color_z_code)

    color_f_name = browser.find_element(
        By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert "alert py-2 alert-success" in color_f_name
    print(color_f_name)

    color_l_name = browser.find_element(
        By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert "alert py-2 alert-success" in color_l_name
    print(color_l_name)

    color_address = browser.find_element(
        By.CSS_SELECTOR, "#address").get_attribute("class")
    assert "alert py-2 alert-success" in color_address
    print(color_address)

    color_city = browser.find_element(
        By.CSS_SELECTOR, "#city").get_attribute("class")
    assert "alert py-2 alert-success" in color_city
    print(color_city)

    color_country = browser.find_element(
        By.CSS_SELECTOR, "#country").get_attribute("class")
    assert "alert py-2 alert-success" in color_country
    print(color_country)

    color_email = browser.find_element(
        By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert "alert py-2 alert-success" in color_email
    print(color_email)

    color_phone = browser.find_element(
        By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert "alert py-2 alert-success" in color_phone
    print(color_phone)

    color_job = browser.find_element(
        By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert "alert py-2 alert-success" in color_job
    print(color_job)

    color_company = browser.find_element(
        By.CSS_SELECTOR, "#company").get_attribute("class")
    assert "alert py-2 alert-success" in color_company
    print(color_company)
