# Задание task_07_02_04.
#
# Выполнил: Глушков Богдан
# Группа: адэу-201



"""
Ошибки (номера строк через пробел): 21 22 24 26 23
в строке 21 делалось умножение, а нам нужна сумма
в строках 21 23 25 переменная не должна называться одноименно с функцией
в строке 22 проход должен идти до предпоследнего числа, иначе улетит за пределы
"""

def min_pair(nums):
    """Вернуть минимальную сумму соседних 2-х чисел в списке 'nums'."""
    min1 = nums[0] + nums[1]
    for i in range(2, len(nums)-1):
        min1 = min(nums[i] + nums[i + 1], min1)

    return min1

l = [1,2,3,4]
print(min_pair(l))
# import random
#
# random.seed(50)
#
# N_MAX = 10
# RANGE_MIN = 1
# RANGE_MAX = 100
# nums = random.sample(range(RANGE_MIN, RANGE_MAX), N_MAX)
#
# print(nums)
#
# print(min_pair(nums))
