# Создать программу, запрашивающую у пользователя два числа и математическую операцию, после чего в зависимости от
# выбранной операции + - / * выполнить указанную операцию
from colorama import init
from colorama import Fore, Back


def calculator():
    init()
    print(Fore.BLACK)
    print(Back.GREEN)
    what = input("Выберите операцию ввиде символа: (+, -, /, *): ")
    print(Back.MAGENTA)
    a = float(input("Введите первое число:"))
    b = float(input("Введите второе число:"))
    if what == "+":
        c = a + b
        print(Back.CYAN)
        print("Результат:" + str(c))
    elif what == "-":
        c = a - b
        print(Back.CYAN)
        print("Результат:" + str(c))
    elif what == "/":
        c = a / b
        print(Back.CYAN)
        print("Результат:" + str(c))
    elif what == "*":
        c = a * b
        print(Back.CYAN)
        print("Результат:" + str(c))
    else:
        print(Back.CYAN)
        print("Выбрана не верная операция")


try:
    calculator()
except:
    print("Ошибка в вводе значений, попробуйте еще раз")
