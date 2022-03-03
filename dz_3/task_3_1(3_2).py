# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.
# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

my_dict = {
            'one': 'один', 
            'two': 'два', 
            'three': 'три', 
            'four': 'четыре', 
            'five': 'пять', 
            'six': 'шесть', 
            'seven': 'семь', 
            'eight': 'восемь', 
            'nine': 'девять', 
            'ten': 'десять'
        }

def num_translate(temp):
    print(my_dict.get(temp, 'None'))
    

def num_translate_adv(temp):
    if temp[0].isupper():
        temp = temp.lower()
        _temp = my_dict.get(temp, 'None')
        print(_temp.capitalize())
    else:
        num_translate(temp)



num_translate('one')
num_translate('two')
num_translate('ones')

num_translate_adv('One')
num_translate_adv('two')
num_translate_adv('threes')


