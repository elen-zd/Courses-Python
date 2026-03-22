from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddProduct:
    def __init__(self, driver):
        """
            Конструктор класса AddProduct,
            для добавления товаров и перехода в корзину
            на сайте www.saucedemo.com.

            :parameter driver: WebDriver — объект драйвера Selenium.
        """
        self._driver = driver

    def page_products(self) -> None:
        """
            Устанавливает неявное ожидание 4 секунды,
            для выполнения операций с элементами на странице.

            Открывает страницу сайта www.saucedemo.com с товарами.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/inventory.html")

    def add_products(self) -> None:
        """
            Последовательное добавление трёх товаров в корзину.


            Для каждого элемента используется явное ожидание до 10 секунд.

            Выполнение операций:
            1. Рюкзак.
            Поиск элемента и нажатие на кнопку добавления в корзину
            2. Футболка.
            Поиск элемента и нажатие на кнопку добавления в корзину
            3. Комбинезон.
            Поиск элемента и нажатие на кнопку добавления в корзину

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        backpack = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
            )
        )
        backpack.click()

        t_shirt = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
            )
        )
        t_shirt.click()

        onesie = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
            )
        )
        onesie.click()

    def basket_enter(self) -> None:
        """
            Переход в корзину.

            Поиск и нажатие на элемент иконки "корзина"
            для перехода на страницу корзины.

            :return: None — метод ничего не возвращает.

            :rtype: None
        """
        basket = self._driver.find_element(
            By.CSS_SELECTOR, "a[data-test=shopping-cart-link]"
        )
        basket.click()
