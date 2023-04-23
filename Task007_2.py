# Задание 2.
#
# Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
# length (длина в метрах), width (ширина в метрах).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
# метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
# Массу и толщину сделать публичными атрибутами.
# Проверить работу метода.
#
# Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т


class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass_calc(self):
        res = self._length * self._width * self.weight * self.thickness
        return int(res)


def user_input():
    while True:
        try:
            val = int(input())
        except ValueError:
            print("Вы ввели строку. Попробуйте ещё раз")
        else:
            return val


print("Ведите длину в метрах: ")
length_roads = user_input()
print("Ведите ширинy в метрах: ")
width_roads = user_input()

asphalt_road = Road(length_roads, width_roads)

print(f'Расчет массы асфальта, необходимого для покрытия всего дорожного полотна: \n{length_roads}м *'
      f' {width_roads} м *{asphalt_road.weight} кг * {asphalt_road.thickness} м = '
      f'{asphalt_road.asphalt_mass_calc()} кг = {asphalt_road.asphalt_mass_calc() // 1000} т')
