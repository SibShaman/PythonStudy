import urllib.request
import xml.etree.ElementTree as ET


def currency_rates(currency_code):
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
        if str(currency_code).upper() == charcode:
            return course
