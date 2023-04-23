"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words_list = ['разработка', 'администрирование', 'protocol', 'standard']


def get_byte_format(list_code):
    list_byte = []
    list_str = []
    for el in list_code:
        byte_l = str.encode(el, encoding='utf-8')
        str_l = bytes.decode(byte_l, encoding='utf-8')
        list_byte.append(byte_l)
        list_str.append(str_l)
    return list_byte, list_str


bytes_list, str_list = get_byte_format(words_list)

print(f'Байтовое представление слов : \n{bytes_list}')
print(f'Строковое представление слов : \n{str_list}')
