# Задание task_04_02_12.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201

a = int(input("a="))
b = int(input("b="))

if(a>b):
    for c in range(b, a + 1):
        print(c, end=" ")
    print("")
    for c in reversed(range(b, a + 1)):
        print(c)
else:
    for c in range(a, b + 1):
        print(c, end=" ")
    print("")
    for c in reversed(range(a, b + 1)):
        print(c)
# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# a = 1
# b = 5
# 1 2 3 4 5
# 5
# 4
# 3
# 2
# 1
