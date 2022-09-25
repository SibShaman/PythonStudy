# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) 
# для получения информации вида: 
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>), например:

# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

import re
from requests import get, utils


responce = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
encodings = utils.get_encoding_from_headers(responce.headers)
content = responce.content.decode(encoding=encodings)


with open('ngnix_logs.txt', 'w+', encoding='utf8') as new_logs:
    new_logs.writelines(content) 

with open('ngnix_logs.txt', 'r', encoding='utf8') as new_logs:
    for line in new_logs:
        _temp = new_logs.readline()

        remote_addr = re.findall(r'^(\w+\.\w+\.\w+\.\w+)', _temp)       
        #remote_addr = re.findall(r'^(([0-9A-Za-z]{3,4}:){6,7})([0-9A-Za-z]{3,4})', _temp)

        request_datetime = re.search(r'\d{1,2}\/\w+\/\d{4}(.)\d{2}(.)\d{2}(.)\d{2}(.{1,6})', _temp)
        request_type = re.search(r'([A-Z]{3})', _temp)
        requested_resource = re.search(r'/\D+(/)\D+.', _temp)
        response_code = re.search(r'\s\d{3}\s', _temp)
        response_size =  re.findall(r'(\s[\d]{1,3}\s")', _temp)
       
       
        parsed_raw = (
            #remote_addr.group(),
            ''.join(remote_addr),
            request_datetime.group(), 
            request_type.group(),
            requested_resource.group(),
            response_code.group().strip(),
            ''.join(response_size).replace('"', '').strip()
        )       

        print(parsed_raw)

    
