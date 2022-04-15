# 5. Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10), 
# а значения  — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }

# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.



import os
import json


folder = 'task_7_5/some_data'


#key_list = [100, 1000, 10000, 100000]
#result_dict = dict.fromkeys(key_list, None)
result_dict = {}

for root, dirs, files in os.walk(folder):
    for file in files:    
        size_to_file = os.stat(os.path.join(root, file)).st_size // 10 *10 +10 # размер файла 
        f_extension = file.rsplit('.')[-1] # расширение

        if size_to_file in result_dict:
            result_dict[size_to_file][1].append(f_extension)
            result_dict[size_to_file] = (result_dict[size_to_file][0] + 1, list(set(result_dict[size_to_file][1])))
        else:
            result_dict.setdefault(size_to_file, (1, [f_extension]))

res = {x: result_dict[x] for x in sorted(result_dict.keys())}
        
with open('task_7_5/task_7_5_summary,json', 'w') as f:
    json.dump(res, f)

