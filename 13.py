# Программирование на языке высокого уровня (Python).
# https://www.yuripetrov.ru/edu/python
# Задание task_03_02_10.
#
# Выполнил: Glushkov
#  Группа: АДЭУ-201


# Создать 2 пустых списка
a = []
b = []

# Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
a.append(4.5)
a.append(3.4)
# Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
a.extend([8.7, 1.3])

# Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
b.append(14.5)
b.append(3.4)

# Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
b.extend([8.7, 11.3])

# Вставить целое число 100 на 2-е и 4-е место списка 'a'
a.insert(1,100)
a.insert(3,100)

# Вставить целое число 200 на 1-е и 3-е место списка 'b'
b.insert(0,200)
b.insert(2,200)

# Вывести списки на экран
print("Исходные списки:")
print(a)
print(b)

# Удалить первые элементы из списков 'a' и 'b'
del a[0]
del b[0]

# Удалить элемент 100 из списка 'a'
a.remove(100)
# Удалить элемент 200 из списка 'b'
b.remove(200)

# Вывести списки на экран
print("\nПосле удалений:")
print(a)
print(b)

# Создать множества из списков 'a' и 'b', а также их пересечение
sa = set(a)
sb = set(b)
sa_and_sb = sa & sb

# Вывести экран уникальные элементы каждого списка и общие
print("\nУникальные элементы:", "1-й:" + str(sa), "2-й:" + str(sb), sep="\n")

print("общие:", sa_and_sb)

# Соединить списки 'a' и 'b'
c = a + b

# Отсортировать список 'c' по возрастанию и убыванию
c_asc = sorted(c)
c_desc = sorted(c, reverse=True)

# Среднее арифметическое элементов списка 'c', расположенных на четных местах
sr_ar = sum(c) # Удалите комментарий и допишите код
# Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
sr_geom = sum(c)  # Удалите комментарий и допишите код

# Максимальный и минимальный элементы
c_max = max(a)# Удалите комментарий и допишите код
c_min = min(b)# Удалите комментарий и допишите код

# Вывести результаты на экран
print("\nИтоговые:")
print("3-й:", c)
print("Сортировка (возр.):", c_asc)
print("Сортировка (убыв.):", c_desc)
print("Макс. и мин.:", c_max, c_min)

# --------------
# Пример вывода:
#
# Исходные списки:
# 1-й: [4.5, 100, 3.4, 100, 8.7, 1.3]
# 2-й: [200, 14.5, 200, 3.4, 8.7, 11.3]
#
# После удалений:
# 1-й: [3.4, 100, 8.7, 1.3]
# 2-й: [14.5, 3.4, 8.7, 11.3]
#
# Уникальные элементы:
# 1-й: {8.7, 1.3, 3.4, 100}
# 2-й: {8.7, 11.3, 3.4, 14.5}
# общие: {8.7, 3.4}
#
# Итоговые:
# 3-й: [3.4, 100, 8.7, 1.3, 14.5, 3.4, 8.7, 11.3]
# Сортировка (возр.): [1.3, 3.4, 3.4, 8.7, 8.7, 11.3, 14.5, 100]
# Сортировка (убыв.): [100, 14.5, 11.3, 8.7, 8.7, 3.4, 3.4, 1.3]
# Ср. арифм. = 29.00, ср. геометр. = 7.82
# Макс. и мин.: 100 1.3