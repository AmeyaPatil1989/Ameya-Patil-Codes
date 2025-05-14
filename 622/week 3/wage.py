hourlywage = float(input('enter hourly wage:'))
overtimehours = float(input('enter overtime hours:'))
regularhours = float(input('enter regular hours:'))

overtimepay= overtimehours * hourlywage * 1.5
emptotalwage = hourlywage * regularhours + overtimepay

print("employees total wage is:", emptotalwage)