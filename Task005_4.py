# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!


def user_input():
    while True:
        try:
            val = int(input("Введите количество элементов: "))
        except ValueError:
            print("Вы ввели строку.")
        else:
            return val


def sum_el(n, s_count=0, x=1):
    if n == 0:
        print(f'Количество элементов - {user_num}, их сумма - {s_count}')
    else:
        s_count = s_count + x
        x = x / (-2)
        sum_el(n - 1, s_count, x)


user_num = user_input()
sum_el(user_num)