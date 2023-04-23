# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

class NegativeNumberError(Exception):
    pass


def user_input():
    while True:
        try:
            val = int(input())
            if val < 0:
                raise NegativeNumberError()
        except NegativeNumberError:
            print("Вы ввели отрицательное число. Попробуйте ещё раз ввести положительное")
        except ValueError:
            print("Вы ввели строку. Попробуйте ещё раз")
        else:
            return val


def sum_num_all(num_1, num_2):
    if num_1 == 0:
        return num_2
    return 1 + sum_num_all(num_1 - 1, num_2)


print('Введите целое число А: ')
numA = user_input()
print('Введите целое число B: ')
numB = user_input()

result = sum_num_all(numA, numB)
print(f'Сумма чисел {numA} и {numB} = {result}')
