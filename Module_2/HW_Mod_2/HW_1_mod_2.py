# ex #1
# <--------------------------------->


# Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
# Сами классы должны соответствовать общему интерфейсу (абстрактному базовому
# классу) SerializationInterface.
# from abc import ABC, abstractmethod
# import json
# import pickle
#
#
# class SerializationInterface(ABC):
#     @abstractmethod
#     def serialise_this(self):
#         pass
#
#
# class SerializationInBin(SerializationInterface):
#     """serialise in bin"""
#     def __init__(self, data):
#         self.data = data
#
#     def serialise_this(self):
#         return pickle.dump(self.data)
#
#
# class SerializationInJson(SerializationInterface):
#     """serialise in json"""
#     def __init__(self, data):
#         self.data = data
#
#     def serialise_this(self):
#         return json.dump(self.data)





# ex #2
# <--------------------------------->


# Напишите класс метакласс Meta, который всем классам для кого он будет
# метаклассом устанавливает порядковый номер. Код для проверки правильности
# решения:




class Meta(type):
    def __new__(cls, name_class, base, atrrib):
        cls.atrrib = {'class_number': cls.children_number}
        cls.children_number += 1
        return type(name_class, base, cls.atrrib)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b= Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
