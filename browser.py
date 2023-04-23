import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

EXE_PATH = r'..\chromedriver.exe'

"""Фикстура с функцией открытия и закрытия браузера"""
@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path=EXE_PATH)
    driver.maximize_window()

    yield driver

    driver.quit()
    print("-" * 40)
    print("\nquit browser...")


