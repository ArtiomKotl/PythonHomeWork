# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.

def user_input():
    while True:
        try:
            val = int(input())
        except ValueError:
            print("Вы ввели строку. Попробуйте ещё раз")
        else:
            return val



def expo_num(num_1, num_2):
    if num_2 == 1:
        return num_1
    return num_1 * expo_num(num_1, num_2 - 1)


print('Введите целое число А: ')
numA = user_input()
print('Введите целое число B: ')
numB = user_input()

result = expo_num(numA, numB)
print(f'{numA} в степени {numB} = {result}')


