# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина * ширина * масса асфальта 
# для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    
    def __init__(self, length, width) -> int:
        self._length = length
        self._width = width

    def calculation_mass(self):
        strip_thickness = 5
        asphalt_weight = 25
        result = (self._length*self._width*strip_thickness*asphalt_weight)/1000
        return f'количество асфальта = {result} тонн'

a = Road(20, 5000)
print(a.calculation_mass())