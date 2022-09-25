"""Представление"""
# Определяет форматы вывода информации в файл
# Принимает какой то словарь и форматирует в зависимости от ТЗ


import json
from typing import Any


def set_kind_contact_one(list_: list) -> Any:
    """Преобразование CSV в JSON - импорт для приведения к формату №1 задания"""
    with open('first_file.json', 'w', encoding='utf8') as file:
        json.dump(list_, file, ensure_ascii=False, indent=2)


def set_kind_contact_two(list_: list) -> Any:
    """Преобразование CSV в JSON - импорт для приведения к формату №2 задания"""
    with open('second_file.json', 'w', encoding='utf8') as file:
        for item in list_:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')
