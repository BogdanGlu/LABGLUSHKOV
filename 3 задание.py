# Задание task_07_02_03.
#
# Выполнил: Глушков Богдан
# Группа: адэу-201


"""
Ошибки (номера строк через пробел, данная строка - №2): 31 35
в строке 31 из-за того, что было больше или равно, выводился последний ряд (ряд перезаписывался), а нам нужен первый 
стр 35 (вовзвращаемая нумерация рядов с 0)
"""
def first_vacant_row(seats):
    """Вернуть первый ряд, в котором имеется больше всего
    свободных мест и их количество.
    Возвращаемая нумерация рядов с 1. Если свободных мест нет, вернуть 0, 0.
    Параметры:
        - seats (list of list): информация о проданных билетах
                                (1 - продано, 0 - нет).
    Результат:
        - tuple (ряд, количество мест).
    """
    max_count = 0
    max_row = 0
    for row_index, row in enumerate(seats):
        available_seats_count = row.count(0)  # 0 - пусто
        if available_seats_count > max_count:
            max_row = row_index
            max_count = available_seats_count

    return max_row + 1, max_count

# import random
#
# random.seed(50)
#
# ROWS_MAX = 10
# SEATS_MAX = 5
#
# seats = [[random.randint(0, 1) for seat in range(SEATS_MAX)]
#                                for row in range(ROWS_MAX)]
#
# for seat in seats:
#     print(seat)
#
# print(first_vacant_row(seats))
