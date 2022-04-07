import sys

with open('bakery.csv', 'a' , encoding='utf8') as add_data:
    add_data.write(f'{sys.argv[1]}\n')
exit()