# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. 
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая. 
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. 
# Сохранить словарь в файл. Проверить сохранённые данные. 
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. 
# Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
        # Иванов,Иван,Иванович
        # Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
        # скалолазание,охота
        # горные лыжи

# 4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ 
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей 
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
#  Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные в результате парсинга.


from itertools import zip_longest


with open('dz_6_3/users.csv', 'r', encoding='utf8') as users, open('dz_6_3/hobby.csv', 'r', encoding = 'utf8') as hobbies,\
        open('dz_6_3/result.csv', 'w', encoding='utf8') as res:             
                        
                for my_key in users:
                        users.seek(0)
                        my_key = users.readlines()                        
                        
                        # парсим из файла Имя, Фамилию и Отчество и сохраняем каждый в отдельный список                        
                        full_name = [i.strip() for i in my_key]
                        first_name_list = []
                        second_name_list = []
                        third_name_list = []
                        for i in full_name:
                                _temp = i.split(" ")
                                # имя
                                first_name = "".join(_temp[1]).replace(',', '')
                                first_name_list.append(first_name)
                                # фамилия
                                second_name = "".join(_temp[0]).replace(',', '')
                                second_name_list.append(second_name)                                
                                # отчество
                                third_name = "".join(_temp[2]).replace(',', '')
                                third_name_list.append(third_name) 
                        # вывод на экран                               
                        print(first_name_list)
                        print(second_name_list)
                        print(third_name_list)


                for my_value in hobbies:
                        hobbies.seek(0)
                        my_value = hobbies.readlines()
                        # по такому же принципу спарсим и все хобби (с записью в отдельный список)
                        all_hobby = [i.strip() for i in my_value]
                        hobby_list = [] 
                        for i in all_hobby:
                                _hobby = i.split(' ')
                                hobby_one = ''.join(_hobby[0]).replace(',', '')
                                hobby_two = ''.join(_hobby[1]).replace(',', '')
                                hobby_list.append(hobby_one)
                                hobby_list.append(hobby_two)
                        print(hobby_list)

                # запишем все данные в отдельный файл                       
                if len(my_key)<len(my_value):
                        print("1")
                else:
                        my_dict = dict(zip_longest(my_key, my_value))
                        for key,val in my_dict.items():
                                res.write('{}:{}\n'.format(key,val))
