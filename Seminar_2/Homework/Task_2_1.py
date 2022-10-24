# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число ')

if number[0] == '-' or number[0] == '+':
    number = number[1:]
if '.' in number:
    number = number.split(sep='.', maxsplit=1)
elif ',' in number:
    number = number.split(sep=',', maxsplit=1)
number_after_check = ''.join(number)

if number_after_check.isdigit():
    result = 0
    for i in range(len(number_after_check)):
        result += int(number_after_check[i])
    print(f'Сумма цифр введенного Вами числа равна {result}')
else:
    print('Число введено некорректно')

# number = float(input('Введите вещественное число '))
# while not number.is_integer():
#     number *=10
#     print(number)