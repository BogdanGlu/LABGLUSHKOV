# Задание task_07_02_05.
# Выполнил: Глушков Богдан
# Группа: адэу-201


"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
Ошибки (номера строк через пробел): 22
for i in range(len(nums)) - тут в качестве индекса использовался сам элемент
"""


def non_negatives(nums):
    """Удалить из списка чисел 'nums' отрицательные элементы и вернуть
    измененный список."""
    for i, n in enumerate(nums):
        if nums[i] < 0:
            del nums[i]

    return nums


print(non_negatives([3, -5, 9, -66, 868687]))

# import random
#
# n = 10
# nums = [round(random.uniform(-10, 10), 2) for i in range(n)]
# print(nums)
#
# non_negatives(nums)
# print(nums)
