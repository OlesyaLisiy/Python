# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

elements_quantity = int(input('Введите количество элементов списка '))

from random import randint

list = []
for i in range(elements_quantity):
    list.append(randint(-elements_quantity, elements_quantity))
print(list)

path = 'file.txt'
with open(path, 'r') as data:
    product = 1
    for position in data:
        product *= list[int(position)]
print(product)
