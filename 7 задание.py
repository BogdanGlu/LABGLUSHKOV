# Задание task_05_02_07.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201

def has_digits(sentence):
    for i in range (0, 10):
        if str(i) in sentence:
            return f'текст с цифрой {i}'
    return 'текст без цифр'

def count(sentence):
    for i in range (0, 10):
        if str(i) in sentence:
            return 1
    return 0

summ = 0
n = int(input("Введите количество предложений: "))
for i in range(1, n + 1):
    o = input(f'Введите предложение №{i} ')
    sentence = o
    print(has_digits(sentence))
    summ += count(sentence);
print(f'Количество предложений с цифрой {summ}')


# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# Введите количество предложений: 3
# Введите предложение №1:
# Просто текст
# Введите предложение №2:
# Текст с цифрой 1 (один)
# Введите предложение №3:
# Тут нет цифры
# Предложений с цифрой = 1
