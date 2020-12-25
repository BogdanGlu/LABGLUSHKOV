# Задание task_07_02_06.
#
# Выполнил: Глушков Богдан
# Группа: адэу-201



"""
Ошибки (номера строк через пробел, данная строка - №2): !!!
"""


def unemployment_rate(unemployed, employed):
    """Вернуть уровень безработицы (УБ) в долях 1.
       Расчет по формуле: УБ = Безработные / (Занятые + Безработные).
    """
    return unemployed / (unemployed + employed)
try:
    unemployed = int(input("Введите кол-во безработных (чел.): "))
    employed = int(input("Введите кол-во занятых (чел.): "))
    rate = unemployment_rate(unemployed, employed)
    print("Уровень безработицы = {:.1%}".format(rate))
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введенные числа.")
except ZeroDivisionError as err:
    print("Ошибка:", err, ". На ноль делить нельзя.")