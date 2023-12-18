import random
print('Добро пожаловать в игру "Угадай число". Нужно угадать целое число от 1 до N.')

def is_valid(str1): # проверка формата ввода данных на целое число
    if str1.isdigit() and float(str1) - int(str1) == 0:
        return True
    else:
        return False

while True:
    right_n = input('Давайте зададим диапазон чисел от 1 до N. Введите N: ')
    if is_valid(right_n):
        n = random.randint(1, int(right_n))  # загадано целое число от 1 до N
        break
    else:
        print('Неправильный формат ввода. Введите целое число')

try_count = 0 # счетчик попыток
game_count = 0 # счетчик игр
flag = True

while flag: # ввод данных, проверка, вывод данных
    input_n = input(f'Введите целое число от 1 до {right_n}: ')
    if is_valid(input_n) and 1 <= int(input_n) <= int(right_n):
        input_n = int(input_n)
        try_count += 1
        if input_n < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif input_n > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print(f'Вы угадали число за {try_count} попыток, поздравляем!')
            try_count = 0
            game_count += 1
            while flag:
                game_over = input('Хотите сыграть ещё раз? Введите 1, если хотите продолжить игру или 0, если хотите закончить игру: ')
                if is_valid(game_over) and 0 <= int(game_over) <= 1:
                    if int(game_over) == 1:
                        n = random.randint(1, int(right_n))
                        break
                    elif int(game_over) == 0:
                        print(f'Вы сыграли {game_count} раз. Игра окончена. Спасибо за игру.')
                        flag = False
                else:
                    print(f'Неправильный формат ввода данных')
    else:
        print(f'Неправильный формат ввода данных. Введите целое число от 1 до {right_n}')