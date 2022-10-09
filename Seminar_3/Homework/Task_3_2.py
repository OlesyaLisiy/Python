# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_of_numbers = [int(element) for element in input(
    'Введите числа через пробел, для завершения ввода нажмите enter ').split()]
result = []
index = 0
while index < len(list_of_numbers)/2:
    result.append(list_of_numbers[index] *
                  list_of_numbers[-1-index])
    index += 1
print(result)