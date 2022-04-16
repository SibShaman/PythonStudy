# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. 
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Рисуем ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Рисуем карандашом'


class Hundle(Stationery):
    def draw(self):
        return f'Рисуем маркером'


a = Stationery(); print(a.draw())
b = Pen(); print(b.draw())
c = Pencil(); print(c.draw())
d = Hundle(); print(d.draw())
