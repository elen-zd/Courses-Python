import pytest
from selenium import webdriver
from pages.Calculator import Calculator
from pages.ShopAuthorize import Authorization
from pages.ShopAddProd import AddProduct
from pages.ShopPageBasket import PageBasket
from pages.ShopFormOrder import FormOrder


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = Calculator(driver)
    calculator.calc_page()
    calculator.field_delay()
    calculator.buttons()
    result = calculator.results()
    assert result == "15"


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(browser):
    shop = Authorization(browser)
    shop.get_page_shop()
    shop.login_user()
    shop.password_user()
    shop.button()

    add_product = AddProduct(browser)
    add_product.page_products()
    add_product.add_products()
    add_product.basket_enter()

    page_basket = PageBasket(browser)
    result = page_basket.check_basket()
    assert result == 3
    page_basket.button_checkout()

    form_order = FormOrder(browser)
    form_order.page_form_order()
    form_order.fill_form_order()
    form_order.page_price_order()
    price_text = form_order.get_price_order()
    assert price_text == "Total: $58.29"
