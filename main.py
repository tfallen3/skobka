import os

menu_options = {
    1: 'Выполнить программу',
    2: 'Информация о программе',
    3: 'Выход',
    4: 'Очистить консоль'
}


def print_menu():           # Вывод кнопок меню
    print('Created by NoName Team. All rights reserved. © Copyright 2022.')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def clearConsole():         # Очистка консоли
    command = 'cls'
    os.system(command)

def option1():
    print('Выполнение программы:', '\n')

    def is_matched(exp):        # функция проверки последовательности скобок
        s = []
        for e in exp:
            if e == '{':
                s.append('}')
            elif e == '[':
                s.append(']')
            elif e == '(':
                s.append(')')
            else:
                if s == [] or e != s[-1]:
                    return False
                s.pop()
        return s == []
    try:
        t = int(input('Введите кол-во чисел в диапазоне 1<n<100000: ').strip())
    except ValueError:
        print('Введена строка или вещественное число')
        print('Повторите выбор кнопки меню, и введите целое число! ')
    if t > 100000:
        print('Введено число больше 100000 или отрицательное: ', t)
    elif t < 1:
        print('Введено число меньше 1 или отрицательное: ', t)
    else:
        for a0 in range(t):
            exp = input('Введите последовательность скобок: ').strip()
            if is_matched(exp):
                print('Yes', '\n'*4)
            elif exp != str:
                print('Введены не скобки!')
            else:
                print("No", '\n'*4)
            break


def option2():
    print('Информация о программе: ')
    print('Название данной программы "Скобки" \n Общие сведения. \n Программа создана компанией NoName Team. Авторы программы: Иванов Александр, Голованов Дмитрий. Адрес компании: г. Красноярск, проспект Имени Газеты Красноярский Рабочий, д. 156. Все права защищены. \n Функциональное назначение программы \n Программа выполняет проверку последовательности состоящию из трёх видов скобок(круглые, квадратные, фигурные), на возможность добавления в нее чисел или знаков арифметических действий так, чтобы получилось правильное арифметическое выражение \n Технические средства \n Персональный Компьютер \n Входные данные \n 1) Целое число от 1 до 100000; 2) Последовательность, состоящая из скобок 3-ёх видов: “()”, “{}”, “[]”. \n Выходные данные \n Yes или No ')


if __name__ == '__main__':
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Введите ваше число: '))
        except ValueError:
            print('Неверный ввод. Введите целое число')
        try:
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                print('Выполняю выход из программы. Спасибо за использование')
                exit()
            elif option == 4:
                clearConsole()
            else:
                print('Неверный выбор выберете между 1 и 4 вкладкой меню. ')
        except UnboundLocalError:
            print('')