class MyMetaClass(type):
    def __init__(cls, *args, **kwargs):
        cls.single_method = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.single_method:
            cls.single_method = super().__call__(*args, **kwargs)
            cls.single_method = cls.single_method = super().__call__(*args, **kwargs)
            return cls.single_method
        else:
            return cls.single_method


class MyClass(metaclass=MyMetaClass):
    def my_method(self):
        pass


obj_1 = MyClass()
obj_2 = MyClass()

print(type(obj_1))
print(type(obj_2))
print(obj_1 == obj_2)
print(obj_1 is obj_2)
