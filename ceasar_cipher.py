rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def int_question_valid(answer):  # функция проверка ввода на целое число
    while True:
        if answer.isdigit() and float(answer) - int(answer) == 0:
            return True
        else:
            return False


def language_valid(text):  # функция проверка ввода на раскладку клавиатуры
    rus_digit = []
    eng_digit = []
    other_digit = []
    for elem in text.lower():
        if elem in rus_alphabet:
            rus_digit.append(elem)
        elif elem in eng_alphabet:
            eng_digit.append(elem)
        else:
            other_digit.append(elem)
    if len(rus_digit) + len(other_digit) == len(text) and int(language_choice) == 1:
        return 1
    elif len(eng_digit) + len(other_digit) == len(text) and int(language_choice) == 2:
        return 2
    else:
        return False


def ceasar_cipher(original):  # функция шифровки
    global cipher
    if int(direction) == 1:
        for i in range(len(original)):
            if original[i].isalpha():
                if original[i].isupper():  # если буква прописная
                    cipher += alphabet[alphabet.find(original[i].lower()) + int(rotation)].upper()
                else:  # если буква строчная
                    cipher += alphabet[alphabet.find(original[i]) + int(rotation)]
            else:
                cipher += original[i]
    elif int(direction) == 2:
        for i in range(len(original)):
            if original[i].isalpha():
                if original[i].isupper():  # если буква прописная
                    cipher += alphabet[alphabet.find(original[i].lower()) - int(rotation)].upper()
                else:  # если буква строчная
                    cipher += alphabet[alphabet.find(original[i]) - int(rotation)]
            else:
                cipher += original[i]
    return cipher


while True:  # выбор направления: шифрование или дешифрование
    direction = input('Выберите направление. Введите 1 для шифрования текста или 2 для дешифрования текста: ')
    if int_question_valid(direction):
        if int(direction) == 1:
            print('Выбрано шифрование')
            break
        elif int(direction) == 2:
            print('Выбрано дешифрование')
            break
        else:
            print('Неправильный формат ввода')
    else:
        print('Неправильный формат ввода')

while True:  # выбор языка: русский или английский
    language_choice = input('Выберите язык. Введите 1 для выбора русского языка или 2 для выбора англиского языка: ')
    if int_question_valid(language_choice):
        if int(language_choice) == 1:
            print('Выбран русский язык')
            break
        elif int(language_choice) == 2:
            print('Выбран английский язык')
            break
        else:
            print('Неправильный формат ввода')
    else:
        print('Неправильный формат ввода')

while True:  # ввод текста
    original = input('Введите текст: ')
    if len(original) > 0 and language_valid(original) == 1:
        alphabet = rus_alphabet
        print("Вы ввели текст на русском языке")
        break
    elif len(original) > 0 and language_valid(original) == 2:
        alphabet = eng_alphabet
        print("Вы ввели текст на английском языке")
        break
    else:
        if int(language_choice) == 1:
            print('Неправильный формат ввода. Введите текст на русском языке')
        elif int(language_choice) == 2:
            print('Неправильный формат ввода. Введите текст на английском языке')

while True:  # ввод сдвига
    rotation = input('Введите ключ сдвига: ')
    if len(rotation) > 0 and int_question_valid(rotation) and int(rotation) > 0:
        break
    elif len(rotation) > 0 and int_question_valid(rotation) and int(rotation) == 0:
        print('Нет сдвига символов')
    else:
        print('Неправильный формат ввода')

cipher = ''

print(ceasar_cipher(original))
