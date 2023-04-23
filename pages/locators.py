from selenium.webdriver.common.by import By

"""Локаторы страницы авторизации"""
class AuthLocators:

    AuthUsername = (By.ID, 'username')#
    AuthPassword = (By.ID, 'password')
    AuthBtnEnter = (By.ID, 'kc-login')
    AuthTabPhone = (By.ID, 't-btn-tab-phone')
    AuthTabMail = (By.ID, 't-btn-tab-mail')
    AuthTabLS = (By.ID, 't-btn-tab-ls')
    AuthTabLogin = (By.ID, 't-btn-tab-login')
    AuthActiveTab = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    AuthLogMail = (By.XPATH, '//*[@id="wrp"]/div[1]/span')
    AuthBtnMAIL = (By.ID, 'oidc_mail')
    AuthBtnVK = (By.ID, 'oidc_vk')
    AuthLogVK = (By.XPATH, '//*[@id="oauth_wrap_content"]/div[2]/div/b')
    AuthBtnOK = (By.ID, 'oidc_ok')
    AuthLogOK = (By.XPATH, '//*[@id="widget-el"]/div[1]/div')
    AuthBtnGOOGLE = (By.ID, 'oidc_google')
    AuthLogGOOGLE = (By.XPATH, '//*[@id="initialView"]/div[2]/div/div[1]/div/div[2]')
    AuthBtnYA = (By.ID, 'oidc_ya')
    AuthLogYA = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/h1/span')
    AuthFormERROR = (By.XPATH, "//span[@id='form-error-message']")#Неверно введен текст с картинки
    AuthMessERROR = (By.CSS_SELECTOR, '.rt-input-container__meta--error')#Надпись Введите номер телефона
    AuthSpaceERROR =(By.XPATH,'//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    AuthRegIn = (By.XPATH, "//a[@id='kc-register']") #Зарегестрироваться
    AuthRegInTempCODE = (By.ID, 'back_to_otp_btn')
    AuthForgotPASSWORD = (By.ID, 'forgot_password')
    AuthHEADING = (By.XPATH, '//*[@id="page-right"]/div/div/h1')



    """Локаторы страницы регистрации"""
class RegLocators:
    RegFIRSTNAME = (By.XPATH, "//input[@name='firstName']")
    RegLASTNAME = (By.XPATH, "//input[@name='lastName']")
    RegREGION = (By.XPATH, "//input[@autocomplete='new-password']"[0])
    RegADDRESS = (By.ID, 'address')
    RegPASSWORD = (By.ID, 'password')
    RegPassCONFIRM = (By.XPATH, "//input[@id='password-confirm']")
    RegREGISTER = (By.XPATH, "//button[@name='register']")
    RegCardMODAL = (By.XPATH, "//h2[@class='card-modal__title']")




    """Локаторы страницы восстановления пароля"""
class NewPassLocators:
    NEW_PASS_ADDRESS = (By.ID, 'username')
    NEW_PASS_BTN_CONTINUE = (By.ID, 'reset')
    NEW_PASS_ONETIME_CODE = (By.XPATH, '//input[@inputmode="numeric"]')
    NEW_PASS_NEW_PASS = (By.ID, 'password-new')
    NEW_PASS_NEW_PASS_CONFIRM = (By.ID, 'password-confirm')
    NEW_PASS_BTN_SAVE = (By.XPATH, '//button[@id="t-btn-reset-pass"]')

class MainPageLocators():
    PAGE_RIGHT = (By.ID, "page-right") #Страница Авторизация