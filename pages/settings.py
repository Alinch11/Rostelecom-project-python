from faker import Faker
import string

valid_firstname = 'Рафаэль'
valid_lastname = 'Санти'
valid_email = 'qa-testit@yandex.ru'
valid_pass = 'Aria1950='


"""Фейковые данные для авторизации в системе"""
invalid_password = '123456710Fk*'
invalid_email = 'asde@mail.ru'
invalid_email2 = 'asПemail.ru'
invalid_phone = '101520'
invalid_firstname = 'Микеланджело'
invalid_lastname = 'Буонарроти'
invalid_ls = '352010008899'







def generate_string_rus(n):
    return 'я' * n

def generate_string_en(n):
    return 's' * n

def english_chars():
    return 'qwertyuiopasdfghjklzxcvbnm'

def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'

def special_chars():
    return f'{string.punctuation}' #Специальные симовлы

def alternative_keyboard():
    return '☺☻♥♦♣♠•◘'
def japanese_hieroglyph():#Японские иероглифы
    return   '原千五百秋瑞'
def chinese_character():# Китайсике иероглифы
    return   '龍門大酒家'
def XSS_admixture_HTML(): #Тестирование на безопасность XSS примесь HTML
    return '<IMG src="#">'
def safety_XSS(): #Тестирование на безопасность XSS инъекция
    return '<script>alert("Поле input уязвимо!")</script>|'
















