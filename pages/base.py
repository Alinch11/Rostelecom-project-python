from pages.config import main_URL
from pages.locators import MainPageLocators
from urllib.parse import urlparse
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cоздаем конструктор, который принимает browser — экземпляр webdriver.
# Указываем base_url, который будет использоваться для открытия страницы.
class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = main_URL
        # команда для неявного ожидания со значением по умолчанию в 5c:
        self.driver.implicitly_wait(timeout)

    # метод go_to_site должен открывать нужную страницу в браузере, используя метод get()
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # создаем метод find_element (ищет один элемент и возвращает его)
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Not find {locator}')

    # создаем метод find_elements (ищет множество элементов и возвращает в виде списка)
    def find_many_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f'Not find {locator}')

    def should_be_menu_authorization(self):
        menu_authorization = self.find_element(*MainPageLocators.PAGE_RIGHT)
        result = menu_authorization.text
        assert result == "Авторизация"

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def find_element_until_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f'Element not clickable!')