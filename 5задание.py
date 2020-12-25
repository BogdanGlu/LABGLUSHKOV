
# Задание task_05_02_05.
#
# Выполнил: Глушков Богдан
# Группа: АДЭУ-201

def is_leap(year):
    l = year - 2000
    if (l % 4) == 0:
        return True
    else:
        return False



def days(month, year):
   if (month == 1) or (month == 4) or (month == 6) or (month == 9) or (month == 11):
       return 30
   if (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
       return 31
   if month == 2:
       if is_leap(year):
           return 29
       else:
           return 28



def previous_date(day, month, year):
    if day == 1:
        if month == 1 or month == 11 or month == 9 or month == 8 or month == 6 or month == 4:
            if month == 1:
                return (31, 12, year - 1)
            else:
                return (31, month - 1, year)
        if month == 12 or month == 10 or month == 7 or month == 5 or month == 2:
            return (30, month - 1, year)
        if month == 3:
            if is_leap(year):
                return (29, month - 1, year)
            else:
                return (28, month - 1, year)
    else:
        return (day - 1, month , year)







def next_date(day, month, year):
    if day == 29:
        if month == 2:
            if is_leap(year):
                return (1, month + 1, year)
            else:
                return("такой даты не существует")
    elif day == 28:
        if month == 2:
            if not (is_leap(year)):
                return (1, month + 1, year)
            else:
                return (day + 1, month, year)
    if day == 30:
        if (month == 1) or (month == 4) or (month == 6) or (month == 9) or (month == 11):
            return (1, month + 1, year)
        else:
            return (day + 1, month, year)
    if day == 31:
        if (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
            if month == 12:
                return (1, 1, year + 1)
            else:
                return (1, month + 1, year)
    else:
        return (day + 1, month, year)






def another_date(day, month, year, delta):
    date = [day, month, year]
    if delta > 0:
        for i in range(0, delta + 1):
            date = next_date(date[0], date[1], date[2])

    elif delta < 0:
        for i in range(0, abs(delta) + 1):
            date = previous_date(date[0], date[1], date[2])
    else:
        return f'Дата остается та же!!!'
    return date


print(is_leap(2030))
print(days(8, 2000))
print(previous_date(1, 2, 2000))
print(next_date(1, 2, 2000))
print(another_date(1, 1, 2000, 9))


# --------------
# Пример вывода:
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): -2
# Новый день: 30/12/1999
#
# День, месяц, год через пробел: 1 1 2000
# Свдиг (может быть отрицательным): 2
# Новый день: 03/01/2000