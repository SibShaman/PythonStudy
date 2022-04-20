
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
#     размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. 
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, size) -> None:
        super().__init__()
        self.size = size
        

    def calculation(self):
        result = float(self.size/6.5 + 0.5)
        return result


class Suit(Clothes):
    def __init__(self, height) -> None:
        super().__init__()
        self.size = height

    @property
    def calculation(self):
        result = float(2*self.size+0.3)
        return result

a = Coat(50)
print(a.calculation())

b = Suit(165)
print(b.calculation)