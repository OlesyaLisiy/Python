# Реализуйте алгоритм перемешивания списка.

from random import shuffle

list_length = input('Введите число элементов списка ')
if list_length.isdigit() and int(list_length) > 1:
    list_length = int(list_length)
    result = []
    for i in range(1, list_length + 1):
        result.append(i)
    print(f'Исходный список при числе элементов, равному {list_length}: \n {result}')
    shuffle(result)
    print(f'Перемешанный список:\n {result}')
else:
    print('Число введено некорректно ')