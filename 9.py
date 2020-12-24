# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_06.
#
# Выполнил: Glushkov
# Группа: АДЭУ-201


a = int(input("введите a="))
b = int(input("введите b="))
m = int(input("введите m="))
n = int(input("введите n="))

x = (0 - b) / a


is_ok = x >= m and x <= n

print("Попадает:", is_ok)


# --------------
# Пример вывода:
#
# Введите a = 1
# Введите b = 2
# Введите m = -5
# Введите n = 5
# Попадает: True
