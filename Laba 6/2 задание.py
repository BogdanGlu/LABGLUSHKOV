
# Задание task_06_02_02.
#
# Выполнил: Глушков богдан
# Группа: АДЭУ-201

# алгоритм разбивает число на цифры и выводит то же число
# сложность O(N+1/2)

def foo(i):
    digits = "0123456789"
    if i == 0: #O(1)
        return "0"
    result = ""
    while i > 0: #O(N)
        result = digits[i%10] + result #O(1)
        i = i // 10 #O(1)
    return result

print(foo(56))
#O(1)+O(N)*(O(1)+O(1))=O(2*N+1)=O(N+1/2)