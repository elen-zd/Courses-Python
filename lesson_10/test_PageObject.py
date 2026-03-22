import pytest
from selenium import webdriver
from pages.Calculator import Calculator
from pages.ShopAuthorize import Authorization
from pages.ShopAddProd import AddProduct
from pages.ShopPageBasket import PageBasket
from pages.ShopFormOrder import FormOrder
import allure


@pytest.fixture
def driver():
    """
        Фикстура для инициализации и завершения работы драйвера Chrome.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def browser():
    """
        Фикстура для инициализации и завершения работы драйвера Firefox.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.suite("Автотесты UI")
@allure.feature("Калькулятор")
@allure.title("Работа калькулятора с задержкой")
@allure.description("Тест проверяет операцию сложения в калькуляторе "
                    "с установленной задержкой 45 секунд.")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятора"):
        calculator = Calculator(driver)
        calculator.calc_page()
    with allure.step("Установить задержку на 45 секунд"):
        calculator.field_delay()
    with allure.step("Выполнить операцию сложения '7+8'"):
        calculator.buttons()
    with allure.step("Получить результат вычисления через 45 секунд"):
        result = calculator.results()
    with allure.step(f"Проверить, что результат равен 15. "
                     f"Ожидаемый результат: '15', "
                     f"Фактический результат: '{result}'"):
        assert result == "15"


@allure.suite("Автотесты UI")
@allure.feature("Интернет-магазин")
@allure.title("Полный сценарий оформления заказа")
@allure.description("Тест проверяет полный цикл работы с интернет-магазином")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(browser):
    with allure.step("Авторизация пользователя в интернет-магазине"):
        with allure.step("Открыть страницу авторизации"):
            shop = Authorization(browser)
            shop.get_page_shop()
        with allure.step("Ввести имя пользователя в поле 'логин'"):
            shop.login_user()
        with allure.step("Ввести пароль пользователя в поле 'пароль'"):
            shop.password_user()
        with allure.step("Нажать кнопку входа в систему"):
            shop.button()

    with allure.step("Добавление товаров в корзину"):
        with allure.step("Открыть страницу с каталогом товаров"):
            add_product = AddProduct(browser)
            add_product.page_products()
        with allure.step("Выбрать и добавить товары в корзину"):
            add_product.add_products()
        with allure.step("Перейти в корзину"):
            add_product.basket_enter()

    with allure.step("Проверка содержимого корзины"):
        with allure.step("Открыть страницу 'Корзина'"):
            page_basket = PageBasket(browser)
            result = page_basket.check_basket()
        with allure.step("Проверить, что количество товаров в корзине "
                         "равно 3"):
            assert result == 3
        with allure.step("Нажать кнопку перехода к оформлению заказа"):
            page_basket.button_checkout()

    with allure.step("Оформление заказа"):
        with allure.step("Открыть страницу формы оформления заказа"):
            form_order = FormOrder(browser)
            form_order.page_form_order()
        with allure.step("Заполнить форму валидными данными пользователя,"
                         "нажать кнопку 'Продолжить'"):
            form_order.fill_form_order()
        with allure.step("Открыть страницу подтверждения заказа"):
            form_order.page_price_order()
        with allure.step("Получить итоговую стоимость заказа"):
            price_text = form_order.get_price_order()
        with allure.step(f"Проверка, что итоговая стоимость равна "
                         f"Total: $58.29. "
                         f"Ожидаемый результат: 'Total: $58.29', "
                         f"Фактический результат: '{price_text}'"):
            assert price_text == "Total: $58.29"
