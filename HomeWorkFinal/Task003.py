"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

words_list = ['attribute', 'класс', 'функция', 'type']


def byte_test(user_list):
    for element in user_list:
        try:
            print(eval(f"b'{element}'"))
        except SyntaxError:
            print(f'Слово: «{element}» невозможно записать в байтовом типе')


byte_test(words_list)
