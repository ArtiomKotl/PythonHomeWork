class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Road'>
        # my_attr - имя атрибута владельца - _length, _length
        self.my_attr = my_attr


class Road:
    weight = 25
    thickness = 0.05
    _length = NonNegative()
    _width = NonNegative()

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
