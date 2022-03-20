# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...) 
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. 
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp. 
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа. 
# Можно ли, используя только методы класса str, решить поставленную задачу? 
# Функция должна возвращать результат числового типа, например float. 
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal? 
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None. 
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

# 3. * (вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера. 
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


import urllib.request
import xml.etree.ElementTree as ET



def currency_rates(numcode):
    URL=urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")
    tree = ET.parse(URL)
    root = tree.getroot()   #корневой элемент

    for valute in root.findall('Valute'):
        # numcode =  int(valute.find('NumCode').text)
        charcode = valute.find('CharCode').text       # получение значений из тегов
        # name = valute.find('Name').text
        nominal =  float(valute.find('Nominal').text)
        value = valute.find('Value').text
        float_value = float('.'.join(value.split(',')))  # перевод текстового значения в тип float
        
        course = float_value/nominal
        if str(numcode).upper() == charcode:
            return course

print(currency_rates('usd'))



# if __name__ == '__main__':
#    test = currency_rates(sys.argv)
#    print(test)
