# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

list_of_numbers = [int(element) for element in input(
    'Введите числа через пробел, для завершения ввода нажмите enter ').split()]
new_list_of_numbers = []
[new_list_of_numbers.append(i) for i in list_of_numbers if i not in new_list_of_numbers]
print(f"Список из неповторяющихся элементов: {new_list_of_numbers}")

