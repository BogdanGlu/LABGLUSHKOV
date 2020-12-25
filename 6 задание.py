# Задание task_05_02_06.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201
def gcd (a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
def gcdn():
    num = [6, 12, 18]
    g = gcd(num[0], num[1])
    for i in range(2, len(num)):
        g = gcd(g, num[i])
    print(f'НОД чисел в списке равен: {g}')
    return g;
def lcm(k,g):
    print(f'НОК чисел в списке равен: {k/g}')


a = gcdn()
k = 0
num = [6, 12, 18]
for i in range(0, len(num)):
    k += num[i]
lcm(k,a);
