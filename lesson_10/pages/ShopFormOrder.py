from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormOrder:
    def __init__(self, driver):
        """
            Конструктор класса FormOrder,
            для перехода на страницу оформления заказа
            на сайте www.saucedemo.com.

            :parameter driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    def page_form_order(self) -> None:
        """
            Открывает страницу с формой оформления заказа
            на сайте www.saucedemo.com.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def fill_form_order(self) -> None:
        """
            Заполнение формы оформления заказа данными пользователя.

            Выполнение операций:
            1. Поле "Имя".
               Используется явное ожидание до 10 секунд.
               Поиск элемента поля "Имя".
               Очищение поля "Имя".
               Ввод данных пользователя в поле "Имя".
            2. Поле "Фамилия".
               Используется явное ожидание до 10 секунд.
               Поиск элемента поля "Фамилия".
               Очищение поля "Фамилия".
               Ввод данных пользователя в поле "Фамилия".
            3. Поле "Почтовый индекс".
               Используется явное ожидание до 10 секунд.
               Поиск элемента поля "Почтовый индекс".
               Очищение поля "Почтовый индекс".
               Ввод данных пользователя в поле "Почтовый индекс".
            4. Кнопка "Continue".
               Поиск элемента кнопки и нажатие на неё.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
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

    def page_price_order(self) -> None:
        """
            Открывает страницу подтверждения заказа,
            со списком добавленных товаров и стоимостью заказа.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        self._driver.get("https://www.saucedemo.com/checkout-step-two.html")

    def get_price_order(self) -> str:
        """
            Получение итоговой стоимости заказа.

            Используется явное ожидание до 10 секунд,
            для отображения итоговой стоимости заказа.

            Поиск элемента итоговой стоимости.

            Переменная с методом извлечения текста
            из элемента итоговой стоимости.

            Возвращение полученного значения в виде строки.

            :return: Отображает текст полученного результата

            :rtype: str - строка
        """
        price_element = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[data-test=total-label]")
            )
        )
        price_total = price_element.text.strip()
        return price_total
