# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, 
# что машина поехала, остановилась, повернула (куда);

# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


from re import T


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name  
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def show_speed(self):
        return f'Автомобиль {self.color} {self.name} едет со скоростью {self.speed}'
    
    def go(self):
       return f'Автомобиль {self.color} {self.name} поехал'

    def stop(self):
        return f'Автомобиль {self.color} {self.name} остановился'

    def direction(self):
        return f'Автомобиль {self.color} {self.name} повернул'


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed>60:
            return f'Автомобиль {self.color} {self.name} превысил скорость и едет {self.speed} км/ч'
        else:
            return super().show_speed()


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed>40:
            return f'Автомобиль {self.color} {self.name} превысил скорость и едет {self.speed} км/ч'
        else:
            return super().show_speed()


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)       

    def show_speed(self):
        if self.speed>80:
            return f'{self.name} Вперед за нарушителем'
        else:
            return super().show_speed()

a = TownCar('Ford', 'черный', 80)
print(a.go()); print(a.show_speed()); print(a.direction()); print(a.stop())
print('\n')
b = WorkCar('MAN', 'желтый', 35)
print(b.go()); print(b.show_speed()); print(b.direction()); print(b.stop())

c = PoliceCar('Maserati', 'белый', 81, is_police=True)
print(c.go()); print(c.show_speed())