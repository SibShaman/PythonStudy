# 41). Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

chek_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

def compression(_str):
    encoding = ''
    prev_char = ''
    count = 1
    if not _str:
        return ''

    for char in _str:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def decompression(_str):
    decode = ''
    count = ''
    for char in _str: # If the character is numerical...
        if char.isdigit(): # ...append it to our count
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


a = compression(chek_str)
print(a)
print(decompression(a))
