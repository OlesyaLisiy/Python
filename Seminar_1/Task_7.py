# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = int(input('Введите число '))

if a%5 == 0 and a%10 == 0 and a%30 != 0:
    print(f'Число {a} кратно 5 и 10 и не кратно 30')
elif a%5 == 0 and a%15 == 0 and a%30 != 0:
    print(f'Число {a} кратно 5 и 15 и не кратно 30')
else:
    print(f'Условие, что число кратно 5 и 10 или 15, но не 30 для введенного числа {a} не выполняется')
