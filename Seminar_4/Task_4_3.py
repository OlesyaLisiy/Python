# Задайте два числа. Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.

# number1, number2 = 6, 8
# nok = max(number1, number2)
# while not (nok % a == 0 and nok % b == 0):  # while nok%a != 0 or nok%b != 0):
#     nok += max(number1, number2)
# print(nok)

a = int(input())
b = int(input())
p = a * b

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
nod = a + b
nok = p // nod
print(nok)