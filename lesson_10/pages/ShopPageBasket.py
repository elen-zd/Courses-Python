from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBasket:
    def __init__(self, driver):
        """
            Конструктор класса PageBasket,
            для перехода на страницу корзины, проверки её содержимого
            и перехода к оформлению заказа

            :parameter driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    def check_basket(self) -> int:
        """
            Открывает страницу "Корзина" на сайте www.saucedemo.com.

            Переменная с методом поиска всех элементов товаров в корзине.

            Возвращает количество товаров найденных в корзине.

            :return: Отображает количество полученного результата

            :rtype: int - число
        """
        self._driver.get("https://www.saucedemo.com/cart.html")

        items = self._driver.find_elements(
                By.CSS_SELECTOR, "div[data-test=inventory-item]"
            )
        return len(items)

    def button_checkout(self) -> None:
        """
            Нажатие на кнопку "Checkout",
            для перехода к оформлению заказа.

            Используется явное ожидание до 10 секунд.

            Поиск элемента кнопки и нажатие на неё.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        button = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#checkout")
            )
        )
        button.click()
