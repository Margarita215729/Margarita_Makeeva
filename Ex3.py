year = int(input('Введите год '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('Это високосный год')
else:
    print('Это невисокосный год')
