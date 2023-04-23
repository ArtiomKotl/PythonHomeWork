"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать
данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, i_list):
        self.i_list = i_list

    def print_matrix(self):
        for el in self.i_list:
            print(el)

    def __str__(self):
        new_string = ''
        for el in self.i_list:
            new_string += str(el) + '\n'
        return new_string

    def __add__(self, other):
        if len(self.i_list) != len(other.i_list):
            exit('Ошибка! Размеры списков не равны! Сложение не возможно')
        res_finish = []
        for i in range(len(self.i_list)):
            res_list = []
            for j in range(len(self.i_list[i])):
                res_list.append(self.i_list[i][j] + other.i_list[i][j])
            res_finish.append(res_list)
        result_obj = Matrix(res_finish)
        return result_obj


# Проверка на ошибку
# array_1 = [[31, 22, 5], [37, 43, 8], [51, 86, 12], [657, 54, 5], [5, 5, 4]]
# array_2 = [[31, 22], [37, 43], [51, 86], [657, 54]]

array_1 = [[31, 22, 5], [37, 43, 8], [51, 86, 12], [657, 54, 5], [5, 5, 4]]
array_2 = [[3, 4, 9], [37, 8, 12], [51, 876, 1], [65, -5, 5], [5, 55, 4]]

mtrx = Matrix(array_1)
mtrx_2 = Matrix(array_2)

print(mtrx.i_list, '\n')
print(mtrx_2.i_list, '\n')
mtrx.print_matrix()                                 # Печать матрицы публичным методом
print()
print(mtrx)                                         # Печать матрицы перегрузкой str
mtrx_2.print_matrix()                               # Печать матрицы публичным методом
print()
print(mtrx_2)                                       # Печать матрицы перегрузкой str

matrix_sum = mtrx + mtrx_2
print(f'Сумма двух матриц: \n{matrix_sum}')

