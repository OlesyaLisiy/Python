# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(n):
    first, second = 0, 1
    fibonacci_num = 0
    for i in range(n):
        fibonacci_num = first + second
        second = first 
        first = fibonacci_num
    return fibonacci_num


def negative_fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2


number = input('Введите число ')
while not number.isdigit():
    number = input('Некорректный ввод. Введите число ')
number = int(number)
list = [0]
for i in range(1, number + 1):
    list.append(fibonacci(i))
    list.insert(0, negative_fibonacci(i))
print(list)
