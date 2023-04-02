# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
#
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.


from sys import argv

employee_calculation, production_hours, rate_hour, premium = argv


def wage(hours, rate, persent):
    #salary = 0
    salary = float(hours) * float(rate)
    prem = (salary / 100) * float(persent)
    print(salary)
    print(prem)
    return prem


premium_per = wage(production_hours, rate_hour, premium)

print(f'выработка в часах - {production_hours} часов')
print(f'ставка в час - {rate_hour} у.е')
print(f'премия - {premium}%')


print('Заработная плата сотрудника (выработка в часах  * ставка в час) + премия = '
      , (float(production_hours) * float(rate_hour)) + float(premium_per))
