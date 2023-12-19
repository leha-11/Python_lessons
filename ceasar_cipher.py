rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'


def int_question_valid(answer):  # проверка ответа на целое число
    while True:
        if answer.isdigit() and float(answer) - int(answer) == 0:
            return True
        else:
            return False


original = input('Введите текст: ')
cipher = ''
rotation = int(input('Введите ключ сдвига: '))

for i in range(len(original)):
    if original[i].isalpha():
        if original[i].isupper():  # если буква прописная
            cipher += rus_alphabet[rus_alphabet.find(original[i].lower()) + rotation].upper()
        else:  # если буква строчная
            cipher += rus_alphabet[rus_alphabet.find(original[i]) + rotation]
    else:
        cipher += original[i]

print(cipher)
