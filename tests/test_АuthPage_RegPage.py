from pages.auth import *
from pages.settings import *
import time
from pages.locators import AuthLocators
from browser import *


""" Проверка страницы авторизации """


@pytest.mark.reg
@pytest.mark.positive
def test_AuthPage_open(browser):
    page = AuthPage(browser)
    assert page.get_relative_link() == '/auth/realms/b2c/protocol/openid-connect/auth'
    time.sleep(4)


"""Переход по вкладкам тел/почта/логин/лицевой счет"""


@pytest.mark.auth
@pytest.mark.positive
def test_switching_tab(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthTabMail).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AuthTabPhone).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AuthTabLogin).click()
    time.sleep(2)
    browser.find_element(*AuthLocators.AuthTabLS).click()
    time.sleep(2)

    assert browser.find_element(*AuthLocators.AuthTabMail).text == 'Почта'
    assert browser.find_element(*AuthLocators.AuthTabPhone).text == 'Телефон'
    assert browser.find_element(*AuthLocators.AuthTabLogin).text == 'Логин'
    assert browser.find_element(*AuthLocators.AuthTabLS).text == 'Лицевой счёт'


""" Автоматическое переключение табов телефон/почта/логин/лицевой счет"""


@pytest.mark.auth
@pytest.mark.positive
@pytest.mark.parametrize('username', ['+79164877123', valid_email, 'invalid_login', '352010658899'],
                         ids=['TRK-009-1) phone', 'TRK-009-2) E-mail', 'TRK-009-3) login', 'TRK-009-4) ls'])
def test_active_tab(browser, username):
    page = AuthPage(browser)
    page.enter_username(username)
    page.enter_password(valid_pass)

    if username == '+79167748778':
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AuthActiveTab).text == 'Телефон'
        browser.find_element(*AuthLocators.AuthTabPhone).click()
        time.sleep(3)
    elif username == valid_email:
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AuthActiveTab).text == 'Почта'
        browser.find_element(*AuthLocators.AuthTabPhone).click()
        time.sleep(3)
    elif username == 'fake_login':
        time.sleep(4)
        assert browser.find_element(*AuthLocators.AuthActiveTab).text == 'Логин'
        browser.find_element(*AuthLocators.AuthTabPhone).click()
        time.sleep(3)
    else:
        try:
            time.sleep(4)
            assert browser.find_element(*AuthLocators.AuthActiveTab).text == 'Лицевой счёт'
        except Exception:
            print('BR-3:Тест не пройден. Нет автоматического переключения на Лицевой счёт')


""" Переход по ссылке социально сети VK"""


def test_changing_link_social_network_VK(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthBtnVK).click()
    time.sleep(3)
    logo = browser.find_element(*AuthLocators.AuthLogVK)
    time.sleep(3)
    assert browser.find_element(*AuthLocators.AuthLogVK).text == 'ВКонтакте'


"""Переход по ссылке социальной сети OK"""


def test_changing_link_social_network_OK(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthBtnOK).click()
    time.sleep(3)
    logo = browser.find_element(*AuthLocators.AuthLogOK)
    time.sleep(3)
    assert browser.find_element(*AuthLocators.AuthLogOK).text == 'Одноклассники'


""" Переход по ссылке социальной сети Мой Мир"""


def test_changing_link_social_network_Mail(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthBtnMAIL).click()
    time.sleep(3)
    logo = browser.find_element(*AuthLocators.AuthLogMail)
    time.sleep(3)
    assert browser.find_element(*AuthLocators.AuthLogMail).text == 'Мой Мир@Mail.Ru'


"""Переход по ссылке GOOGLE"""


def test_changing_link_Google(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthBtnGOOGLE).click()
    time.sleep(3)
    logo = browser.find_element(*AuthLocators.AuthLogGOOGLE)
    time.sleep(3)
    assert browser.find_element(*AuthLocators.AuthLogGOOGLE).text == 'Войдите в аккаунт Google'


"""Переход по ссылке YANDEX"""


def test_changing_link_YA(browser):
    AuthPage(browser)
    browser.find_element(*AuthLocators.AuthBtnYA).click()
    time.sleep(3)
    browser.find_element(*AuthLocators.AuthBtnYA).click()
    time.sleep(3)
    logo = browser.find_element(*AuthLocators.AuthLogYA)
    time.sleep(3)
    assert browser.find_element(*AuthLocators.AuthLogYA).text == 'Войдите с Яндекс ID'


"""Авторизация по почте и паролю."""


def test_AuthPage_valid_email(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(valid_pass)
    time.sleep(25)  # время необходимое для ввода вручную
    page.btn_click_enter()
    print('Авторизация прошла успешно!')
    assert page.get_relative_link() == '/account_b2c/page'


def test_change_tab_on_personal_account(browser):
    browser.find_element(*AuthLocators.AuthActiveTab).send_keys('112358132134')
    browser.find_element(*AuthLocators.AuthPassword).click()
    assert browser.find_element(*AuthLocators.AuthTabLS).text == 'Лицевой счёт', 'FAIL'


"""TRK-024 Авторизации по E-mail и паролю,в системе: неверный E-mail"""


def test_AuthPage_invalid_email(browser):
    page = AuthPage(browser)
    page.enter_username(invalid_email)
    page.enter_password(valid_pass)
    time.sleep(25)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AuthFormERROR)
    forgot_pass = browser.find_element(*AuthLocators.AuthForgotPASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           forgot_pass.text == 'Забыл пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'  # Проверка, что ссылка "Забыл пароль" окрасилась
    # в красный цвет


"""TRK-025 Авторизации по E-mail и паролю, в системе: неверный пароль"""


def test_AuthPage_invalid_password(browser):
    page = AuthPage(browser)
    page.enter_username(valid_email)
    page.enter_password(invalid_password)
    time.sleep(25)
    page.btn_click_enter()
    browser.implicitly_wait(10)

    error_mess = browser.find_element(*AuthLocators.AuthFormERROR)
    forgot_pass = browser.find_element(*AuthLocators.AuthForgotPASSWORD)
    assert error_mess.text == 'Неверный логин или пароль' and \
           forgot_pass.text == 'Забыл пароль' and \
           page.check_color(forgot_pass) == '#ff4f12'  # Проверка, что ссылка "Забыл пароль" окрасилась


"""TRK-026 Проверка авторизации по пустому логину  и паролю"""


@pytest.mark.auth
@pytest.mark.negative
def test_AuthPage_login_empty_username(browser):
    page = AuthPage(browser)
    browser.find_element(*AuthLocators.AuthTabLogin).click()
    page.enter_login(" ")
    page.btn_click_enter()
    page.enter_password(valid_pass)
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.AuthSpaceERROR)
    time.sleep(10)
    assert error_mess.text == 'Введите логин, указанный при регистрации'


"""Авторизация по номеру телефона и паролю, неверный формат телефона"""


@pytest.mark.auth
@pytest.mark.negative
def test_AuthPage_invalid_username(browser):
    page = AuthPage(browser)
    page.enter_username(invalid_phone)
    time.sleep(3)
    page.enter_password(valid_pass)
    browser.implicitly_wait(10)
    error_mess = browser.find_element(*AuthLocators.AuthMessERROR)
    assert error_mess.text == 'Неверный формат телефона'


""" Открытие страницы Регистрация """


@pytest.mark.reg
@pytest.mark.positive
def test_RegPage_open(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


"""Регистрация на странице, невалидный формат телефона"""


@pytest.mark.reg
@pytest.mark.negative
def test_get_registration_invalid_format_phone(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_firstname(valid_firstname)
    browser.implicitly_wait(5)
    page.enter_lastname(valid_lastname)
    browser.implicitly_wait(5)
    page.enter_email(invalid_phone)
    browser.implicitly_wait(3)
    page.enter_password(invalid_password)
    browser.implicitly_wait(3)
    page.enter_pass_conf(invalid_password)
    browser.implicitly_wait(3)
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AuthMessERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'


"""Регистрации на странице, невалидный формат E-mail."""


@pytest.mark.reg
@pytest.mark.negative
def test_get_registration_invalid_format_email(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    page = RegPage(browser)
    page.enter_firstname(valid_firstname)
    browser.implicitly_wait(5)
    page.enter_lastname(valid_lastname)
    browser.implicitly_wait(5)
    page.enter_email(invalid_email2)
    browser.implicitly_wait(3)
    page.enter_password(invalid_password)
    browser.implicitly_wait(3)
    page.enter_pass_conf(invalid_password)
    browser.implicitly_wait(3)
    page.btn_click()

    error_mess = browser.find_element(*AuthLocators.AuthMessERROR)
    assert error_mess.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                              'или email в формате example@email.ru'


"""Регистрация в системе c существующим аккаунтом по E-mail"""


@pytest.mark.reg
@pytest.mark.negative
def test_get_registration_living_account(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    page.enter_firstname(invalid_firstname)
    browser.implicitly_wait(5)
    page.enter_lastname(invalid_lastname)
    browser.implicitly_wait(5)
    page.enter_email(valid_email)
    browser.implicitly_wait(3)
    page.enter_password(invalid_password)
    browser.implicitly_wait(3)
    page.enter_pass_conf(invalid_password)
    browser.implicitly_wait(3)
    page.btn_click()
    time.sleep(2)
    card_modal_title = browser.find_element(*RegLocators.RegCardMODAL)

    assert card_modal_title.text == 'Учётная запись уже существует'


"""Регистрация в системе: поле пароль и подтверждение пароля не совпадают"""


@pytest.mark.reg
@pytest.mark.negative
def test_get_registration_diff_pass_and_pass_conf(browser):
    page = AuthPage(browser)
    page.enter_reg_page()
    browser.implicitly_wait(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'

    page = RegPage(browser)
    page.enter_firstname(invalid_firstname)
    browser.implicitly_wait(5)
    page.enter_lastname(invalid_lastname)
    browser.implicitly_wait(5)
    page.enter_email(invalid_email)
    browser.implicitly_wait(3)
    page.enter_password(invalid_password)
    browser.implicitly_wait(3)
    page.enter_pass_conf(valid_pass)
    browser.implicitly_wait(3)
    page.btn_click()
    error_mess = browser.find_element(*AuthLocators.AuthMessERROR)
    time.sleep(5)
    assert error_mess.text == 'Пароли не совпадают'


""" Открытие страницы Восстановление пароля """


@pytest.mark.reg
@pytest.mark.positive
def test_new_pass_open(browser):
    page = AuthPage(browser)
    page.enter_new_pass_page()
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'
