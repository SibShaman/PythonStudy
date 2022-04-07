# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).
#  Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

from requests import get, utils


responce = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(responce.headers)
content = responce.content.decode(encoding=encodings)


with open('task_6_1(6_2)/ngnix_logs.txt', 'w+', encoding='utf8') as new_logs:
    new_logs.writelines(content) 

with open('task_6_1(6_2)/ngnix_logs.txt', 'r', encoding='utf8') as new_logs:
    for line in new_logs:
        _temp = new_logs.readline()
        _index = _temp.replace('"', ' ').split(' ')
        print((_index[0], _index[6], _index[7]))
    

# 2. Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.

with open('task_6_1(6_2)/ngnix_logs.txt', 'r', encoding='utf8') as spam:
    ip_sent_requests = [line[:line.find(' ')] for line in spam]

max_requests = max(set(ip_sent_requests), key=ip_sent_requests.count)
print('максимальное количество запросов было с адреса: {} , Количество запросов: {}'.format(max_requests, ip_sent_requests.count(max_requests)))
