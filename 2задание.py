# Задание task_05_02_02.
#
# Выполнил: Глушков Богдан
# Группа: АДЭу-201



def avg(data):
    l = 0
    o = 0
    for i in data:
        l += float(i)
        o += 1
    return l / o

def cleared_data(data):
   spisok = []
   for i in data:
       if i != None:
           spisok.append(i)
   return(spisok)


data = []

n = int(input("количество измерений: "))
for i in range(1, n + 1):
    buff = input("измерение " + str(i) + "-е: ")
    data.append(buff if buff.isdigit() else None)
    i += 1

data = cleared_data(data)

print("средняя температура: " + str(avg(data)))




# Удалите комментарий и допишите код

# Получить очищенный список и среднее значение
# Удалите комментарий и допишите код

# --------------
# Пример вывода:
#
# Кол-во измерений: 3
# Измерение 1-е: 10
# Измерение 2-е: -
# Измерение 3-е: 20
# Средняя температура: 15.00
