# 41). Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

import itertools



chek_str = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'


def compression_one(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)
        yield char if count == 1 else str(count)+char


def compression_two(_str):
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
    decoding = ''
    count = ''
    for char in _str:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding


print(*compression_one(chek_str))
a = compression_two(chek_str)
print(a)
print(decompression(a))
