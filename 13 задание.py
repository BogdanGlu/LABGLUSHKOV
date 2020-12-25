# Задание task_04_02_13.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201


a = int(input("a="))
b = int(input("b="))
n_sum = 0
n_mult = 1
n = 0
n_avg = 0
n_avg_geom = 0
for c in range (a, b + 1):
    n_sum += c
print("Сумма =", n_sum)

for c in range (a, b + 1):
    n_mult *= c
print("Произведение =", n_mult)
for c in range (a, b + 1):

    n += 1
    n_avg = n_sum / n
for c in range (a, b + 1):
    if c % 2 == 1:
        n_avg_geom = n_mult ** (1 / n)
print("Среднее арифметическое = {frog}".format(frog = n_avg))
print("Среднее геометрическое нечетных чисел = {dog}".format(dog = n_avg_geom))

# --------------
# Пример вывода:
#
# a = 1
# b = 5
# Сумма = 15
# Произведение = 120
# Среднее арифметическое = 3.00
# Среднее геометрическое нечетных чисел = 2.47
