"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""


import yaml

dict_to_write = {'my_list': ['notebook', 'monitor', 'keyboard', 'mouse', 'headset'],
                 'num_int': 150,
                 'dict_price': {'notebook': '900\u20AC', 'monitor': '150\u20AC', 'keyboard': '30\u20AC',
                                'mouse': '15\u20AC', 'headset': '30\u20AC'}}

with open('file.yaml', 'w', encoding="utf-8") as f_n:
    yaml.dump(dict_to_write, f_n, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r', encoding="utf-8") as f_n:
    print(f_n.read())
