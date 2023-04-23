"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

link_list = (['ping', 'yandex.ru'], ['ping', 'youtube.com'])


def type_converter(args):
    ping_process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ping_process.stdout:
        answer = chardet.detect(line)
        result = line.decode(answer['encoding']).encode('utf-8')
        result = result.decode('utf-8')
        print(result)


for item in link_list:
    type_converter(item)
