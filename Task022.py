# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

def set_range(elem):
    set_0 = set()
    for i in range(elem):
        set_0.add(int(input(f'Введите {i+1} элемент: ')))
    return set_0


elem_n = int(input('Введите количество элементов первого множества: '))
elem_m = int(input('Введите количество элементов второго множества: '))

set_first = set_range(elem_n)
set_second = set_range(elem_m)

print(f'Первое множество \n {set_first}')
print(f'Второе множество \n {set_second}')
inter_set = sorted(set_first.intersection(set_second))
print(f'Числа, которые встречаются в обоих наборах: \n {inter_set}')
