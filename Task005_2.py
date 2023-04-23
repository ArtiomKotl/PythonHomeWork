# Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).
# Подсказка:
# На каждом шаге вам нужно 'доставать' из числа очередную цифру
# и смотреть является ли она четной или нечетной.
# При этом увеличиваем соответствующий счетчик
# Пока все числа не извлечены, рекурсивные вызовы продолжаем
# Условие завершения рекурсии - все числа извлечены
# Используем операции % //. Операции взятия по индексу применять нельзя.
# Решите через рекурсию. В задании нельзя применять циклы.
# Пример:
# Введите число: 123
# Количество четных и нечетных цифр в числе равно: (1, 2)

class NotNaturalNumberError(Exception):
    pass


def user_input():
    while True:
        try:
            val = int(input("Введите число: "))
            if val < 0:
                raise NotNaturalNumberError()
        except NotNaturalNumberError:
            print("Вы ввели отрицательное значение: ")
        except ValueError:
            print("Вы ввели строку.")
        else:
            return val


def even_odd_count(num, count_1=0, count_2=0):
    if num == 0:
        print(f'Количество четных и нечетных цифр в числе равно: {count_1}, {count_2}')
    else:
        n = num % 10
        if n % 2 == 0:
            even_odd_count(num // 10, count_1 + 1, count_2)
        else:
            even_odd_count(num // 10, count_1, count_2 + 1)


user_num = user_input()
even_odd_count(user_num)
