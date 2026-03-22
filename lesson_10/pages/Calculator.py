from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator:
    def __init__(self, driver):
        """
            Конструктор класса Calculator
             для взаимодействия с калькулятором на веб-странице.

            :parameter driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    def calc_page(self) -> None:
        """
            Открывает страницу калькулятора в браузере.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        self._driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html")

    def field_delay(self) -> None:
        """
            Установка задержки для выполнения операций на калькуляторе.

            Находит элемент поля задержки по локатору.

            Очищает поле задержки.

            Устанавливает значение 45 секунд в поле задержки.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        field_del = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#delay"))
        )
        field_del.clear()
        field_del.send_keys("45")

    def buttons(self) -> None:
        """
            Выполняет последовательное нажатие кнопок калькулятора.

            Выполнение операций:
            1. Нажатие на кнопку "7"
            2. Нажатие на кнопку "+"
            3. Нажатие на кнопку "8"
            4. Нажатие на кнопку "="

            :return: None — метод ничего не возвращает

            :rtype: None
        """
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[1]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[4]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[2]").click()
        self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[2]/span[15]").click()

    def results(self) -> str:
        """
            Получение результата вычисления.

            Ожидает отображение результата "15" в течение 45 секунд.

            Получает значение элемента результата.

            Возвращает полученный результат.

            :return: Отображает текст полученного результата

            :rtype: str - строка
        """
        WebDriverWait(self._driver, 45).until(
            EC.text_to_be_present_in_element(
                (By.XPATH, "//*[@id='calculator']/div[1]/div"), "15")
        )
        result = self._driver.find_element(
            By.XPATH, "//*[@id='calculator']/div[1]/div")
        return result.text
