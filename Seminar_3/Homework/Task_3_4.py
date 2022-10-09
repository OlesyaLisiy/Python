# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_bin(number):
    number_initial = int(number)
    result = ''
    while number_initial != 0:
        result = str(number_initial % 2) + result
        number_initial //=2
    return result

number = input('Введите число ')
while not number.isdigit():
    number = input('Некорректный ввод. Введите число ')
print(f'Число {number} в двоичном исчислении будет числом {decimal_to_bin(number)}')