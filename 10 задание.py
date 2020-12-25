# Задание task_05_02_10.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201



def sentence_stats(sentence):
    d = True
    result = list(s)
    spisok = []
    for i in result:
        n = result.count(i)
        t = f'{i}: {n}'
        spisok.append(t)
    spisok2 = []
    for m in spisok:
        d = True
        for j in spisok2:
            if m == j:
                d = False
        if d:
            spisok2.append(m)

    return spisok2


s = input('Введите предложение: ')


print(sentence_stats(s))




# --------------
# Пример вывода:
#
# Введите предложение: мама МЫла РамУ
# {'л': 1, 'р': 1, 'у': 1, 'м': 4, 'а': 4, 'ы': 1, ' ': 2}
