"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по
окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают
 разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод,
которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
from random import randint


def find_max(mylist):
    maximum = my_list[0] + my_list[1] + my_list[2]
    summa = 0
    for i in range(len(my_list)):
        summa = my_list[i] + my_list[(i + 1) % len(my_list)] + my_list[(i + 2) % len(my_list)]
        if summa > maximum:
            maximum = summa
    print(f"Максимальное число ягод равно: {maximum}")


def create_list(n):
    list_1 = list()
    for i in range(n):
        list_1.append(randint(1, 10))
    return list_1


my_list = create_list(15)
print(my_list)
find_max(my_list)