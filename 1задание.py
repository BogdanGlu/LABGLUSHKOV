
# Задание task_05_02_01.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201

x = float(input("введи х:"))
y = float(input("введи у:"))

def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return 0
    else:
        return -1

def sgn(y):
    if y > 0:
        return 1
    elif y == 0:
        return 0
    else:
        return -1


u = sgn(x) + y ** 2
t = sgn(y) - (abs(x)) ** 0.5
z = u / t







print("Ответ:" + str(round(z, 2)))

# --------------
# Пример вывода:
#
# Введите x: -9
# Введите y: 0
# Ответ: 0.33