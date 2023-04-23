"""
Задание 1.

Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.

*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def get_code_points(list_code):
    c_p_array = []
    for el in list_code:
        temp = (el.encode("unicode_escape", "utf-8"))
        c_p_array.append(temp.decode('utf-8'))
    return c_p_array


def conversion_print(word_list, points_list):
    for i in range(len(word_list)):
        print(f'"{word_list[i]}" - буквенный формат.')
        print(f'Тип данных: {type(word_list[i])}')
        print(f'{points_list[i]} - набор кодовых точек')
        print(f'Тип данных: {type(points_list[i])}\n')


words = ['разработка', 'сокет', 'декоратор']

code_points = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

print(words is code_points)
print(words == code_points)
print(type(words))
print(type(code_points))

code_points_arr = get_code_points(words)

conversion_print(words, code_points_arr)


