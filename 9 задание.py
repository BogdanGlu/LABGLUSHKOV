# Задание task_04_02_09.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201


a = float(input("a="))
n = 0.0
x_sum = 0

while (x_sum) <= a:
    n += 1
    x_sum += (1 / n)
else:
    print("n=" + str(n))

# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# a = 1.5
# n = 3
#
# a = 2
# n = 4