# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов 
# список с сохранением порядка их следования в исходном списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = set()
_tmp = set()
for element in src:
    if element not in _tmp:
        result.add(element)
    else:
        result.discard(element)
    _tmp.add(element)

result_sort = [element for element in src if element in result]
print(result_sort)
