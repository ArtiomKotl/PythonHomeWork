"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

format_bytes = [b'class', b'function', b'method']


def get_results(user_list):
    for element in user_list:
        print(f'Тип: {type(element)} | Содержимое: {element} | Длина: {len(element)}')


get_results(format_bytes)
