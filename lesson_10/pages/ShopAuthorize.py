from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Authorization:
    def __init__(self, driver):
        """
            Конструктор класса Authorization,
            для перехода на страницу авторизации
            и заполнения данных пользователя

            :parameter driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    def get_page_shop(self) -> None:
        """
            Устанавливает неявное ожидание 4 секунды,
            для выполнения операций с элементами на странице.

            Открывает страницу авторизации сайта www.saucedemo.com,
            с формой для ввода данных.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/")

    def login_user(self) -> None:
        """
            Заполнение поля "логин".

            Используется явное ожидание до 10 секунд.

            Поиск поля "логин" по локатору элемента.

            Очищение поля "логин".

            Ввод имени пользователя в поле "логин".

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        log_user = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#user-name"))
        )
        log_user.clear()
        log_user.send_keys("standard_user")

    def password_user(self) -> None:
        """
            Заполнение поля "пароль".

            Используется переменная со значением пароля

            Используется явное ожидание до 10 секунд.

            Поиск поля "пароль" по локатору элемента.

            Очищение поля "пароль".

            Ввод пароля пользователя в поле "пароль" из переменной.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        password = "secret_sauce"
        pass_user = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#password")
            )
        )
        pass_user.clear()
        pass_user.send_keys(password)

    def button(self) -> None:
        """
            Нажимает кнопку для входа в систему.

            Используется явное ожидание до 10 секунд,
            для отображения кнопки входа.

            Поиск и нажатие кнопки для входа в систему.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        button_login = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#login-button")
            )
        )
        button_login.click()
