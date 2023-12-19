from random import choice

psw_chars = ''
psw = ''


def int_question_valid(answer):  # проверка ответа на целое число
    while True:
        if answer.isdigit() and float(answer) - int(answer) == 0:
            return True
        else:
            return False


def str_question_valid(answer):  # проверки ответа да/нет
    if answer.isalpha() and (answer.lower() == 'да' or answer.lower() == 'yes'):
        return 'да'
    elif answer.isalpha() and (answer.lower() == 'нет' or answer.lower() == 'no'):
        return 'нет'


def generate_password(length, chars):  # генератор паролей
    global psw
    for _ in range(int(length)):
        psw += choice(chars)
    return psw


while True:
    psw_quantity = input('Сколько паролей нужно сгенерировать: ')
    if int_question_valid(psw_quantity):
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_len = input('Укажите длину пароля: ')
    if int_question_valid(psw_len):
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_digits = input('Включить в пароль цифры 0123456789 ? ')
    if str_question_valid(psw_digits) == 'да':
        psw_chars += '0123456789'
        break
    elif str_question_valid(psw_digits) == 'нет':
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_uppercase_letters = input('Включить в пароль прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? ')
    if str_question_valid(psw_uppercase_letters) == 'да':
        psw_chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        break
    elif str_question_valid(psw_uppercase_letters) == 'нет':
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_lowercase_letters = input('Включить в пароль строчные буквы abcdefghijklmnopqrstuvwxyz ? ')
    if str_question_valid(psw_lowercase_letters) == 'да':
        psw_chars += 'abcdefghijklmnopqrstuvwxyz'
        break
    elif str_question_valid(psw_lowercase_letters) == 'нет':
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_symbols = input('Включить в пароль символы !#$%&*+-=?@^_ ? ')
    if str_question_valid(psw_symbols) == 'да':
        psw_chars += '!#$%&*+-=?@^_'
        break
    elif str_question_valid(psw_symbols) == 'нет':
        break
    else:
        print('Неправильный формат ввода')

while True:
    psw_exceptions = input('Исключить из пароля неоднозначные символы 0oO1iIlL ? ')
    if str_question_valid(psw_exceptions) == 'да':
        for char in '0oO1iIlL':
            psw_chars = psw_chars.replace(char, '')
        break
    elif str_question_valid(psw_exceptions) == 'нет':
        break
    else:
        print('Неправильный формат ввода')

print(f'Из набора символов {psw_chars} сгенерировано {psw_quantity} паролей длиной {psw_len} символов:')

for _ in range(int(psw_quantity)):
    generate_password(psw_len, psw_chars)
    print(psw)
    psw = ''

