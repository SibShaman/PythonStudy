# 38). Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
# 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные:
# 'лповап ываываыв'

original_string = 'ываабв лповап абвцукв алоабвабв ываываыв'
remove_element = 'абв'
temp_list = original_string.split(' ')
res_list = []
for i in range(len(temp_list)):
    if remove_element not in temp_list[i]:
        res_list.append(temp_list[i])
res_str = ' '.join(res_list)

print(res_str)