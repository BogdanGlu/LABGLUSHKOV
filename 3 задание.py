
# Задание task_04_02_03.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201


a = int(input())
b = int(input())
d = int(input())
fix = 1
a1 = a + fix
b1 = b + fix



if (a >= 0 and b >= 0 and d >= 0):
    if (a1 < d and b1 < d):
        print("ДА")
else:
    print("НЕТ")





# --------------
# Пример вывода:
#
# Ширина форточки: 5
# Высота форточки: 6
# Диаметр головы: 6
# Нет

# Ширина форточки: 6
# Высота форточки: 7
# Диаметр головы: 4
# Да