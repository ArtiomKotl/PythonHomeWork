goods = []
number = 0

print('Введите одной строкой название товара, цену, количество и единицу измерения')
print('В качестве разделителя позиций исполльзуйте запятую')
print('Значения цены и количества должны быть целочисленными')
print('Для завершения введите пустую строку')

while True:
    number += 1
    good_list = input(f'{number} товар: ').split(',')
    if good_list == ['']:
        break

    goods.append((number, {'Название': good_list[0],
                           'Цена': int(good_list[1]),
                           'Количество': int(good_list[2]),
                           'Ед. изм.': good_list[3]}))

print(f"Исходный список товаров: \n{goods}")
# Результирующий словарь
goods_dict = {}

for i, el in enumerate(list(goods[0][1].keys())):
    # Собираем для нового словаря названия ключей из первой строки goods
    goods_dict[el] = []

for i, el in enumerate(goods_dict):
    # Пустой список, в который будем записывать значения по каждому ключу
    dict_list = []

    # Собираем значения для текущего ключа результирующего словаря
    for j, el_goods in enumerate(goods):
        key_val = el_goods[1].get(el)

        # Добавляем, только если значения нет в списке
        if key_val not in dict_list:
            dict_list.append(key_val)

    # Записываем в результирующий словарь значение текущего ключа
    goods_dict[el] = dict_list

print("Отчет по списку товаров: ")
for k, v in goods_dict.items():
    print(k, v)
