print('Структура «Рейтинг»')
print('Для звершения программы введите: -1')
rating_list = [7, 5, 3, 3, 2]
print(rating_list)
new_num = int(input('Введите новый элемент рейтинга: '))
while new_num != -1:
    for el in rating_list:
        if new_num > el:
            rating_list.insert((rating_list.index(el)), new_num)
            print(rating_list)
            break
        elif new_num <= min(rating_list):
            el = min(rating_list)
            rating_list.insert((rating_list.index(el) + 1), new_num)
            print(rating_list)
            break
    new_num = int(input('Введите новый элемент рейтинга: '))
print(rating_list)
