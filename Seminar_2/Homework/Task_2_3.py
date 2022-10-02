# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = input('Введите натуральное число ')

if number.isdigit() and int(number) > 0:
    number = int(number)
    result = dict()
    for i in range(1, number + 1):
        result[i] = (1+1/i)**i
    print(f'{result}')
    sum = 0
    for i in result:
        sum += result[i]
    print(f'Сумма последовательности (1+1/{number})^{number} равна {sum}')
else:
    print("Число введено некорректно")
