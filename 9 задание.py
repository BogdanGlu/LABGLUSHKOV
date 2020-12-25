# Задание task_05_02_09.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201


LETTERS_EX = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
DIGITS_EX = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_base(number, base):
    answer = []
    while number > 0:
        t = number % base
        number = number // base
        answer.append(t)
    for n, i in enumerate(answer):
        if(i >= 10):
            answer[n] = LETTERS_EX.get(i)
    answer.reverse()
    return answer


def from_base(number, base):
    summ = 0
    for n, i in enumerate(reversed(number)):
        if(DIGITS_EX.get(i) != None):
            summ += DIGITS_EX.get(i) * (base ** n)
        else:
            summ += int(i) * (base ** n)
    return summ




k = int(input('введите число в десятичной системе счисления: '))
z = int(input('введите основание нового числа: '))
print(to_base(k, z))
p = input('введите число:')
j = int(input('назовите систему счисления числа: '))

print(from_base(p, j))

