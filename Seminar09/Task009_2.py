class TypedProperty:
    def __init__(self, name, type_name, default=None):
        self.name = "_" + name
        self.type = type_name
        self.default = default if default else type_name()

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Ошибка типа данных, введите строку" % self.type)
        setattr(instance, self.name, value)


class Worker:
    name = TypedProperty("name", str)
    surname = TypedProperty("surname", str)

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

worker_2 = Position(123, 'Остапова', 'Кладовщик')         #Проверка на TypeError
print(worker_2.get_full_name())
