# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
# str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 40000, "bonus": 5000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        res = sum(self._income.values())
        return res

    def __str__(self):
        return f"{self.name} {self.surname}. Должность: - {self.position}"


worker = Position('Евгений', 'Иванов', 'Крановщик')
print(worker.get_full_name())
print('дохода с учетом премии: ', worker.get_total_income())
print(worker)
print(worker.__dict__)

worker_2 = Position('Наталья', 'Остапова', 'Кладовщик')
print(worker_2.get_full_name())
worker_2._income = {"wage": 50000, "bonus": 15000}
print('дохода с учетом премии: ', worker_2.get_total_income())
print(worker_2)
print(worker_2.__dict__)
