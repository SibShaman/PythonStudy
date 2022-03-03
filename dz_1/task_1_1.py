# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

duration = int(input("Введите количество времени в секундах "))

days = duration // seconds_in_day
duration = duration - (days * seconds_in_day)

hours = duration // seconds_in_hour
duration = duration - (hours * seconds_in_hour)

minutes = duration // seconds_in_minute
duration = duration - (minutes * seconds_in_minute)


result = ("{} дн ".format(days) if days else "") + \
         ("{} час ".format(hours) if hours else "") + \
         ("{} мин ".format(minutes) if minutes else "") + \
         ("{} сек ".format(duration) if duration else "")
print(result)