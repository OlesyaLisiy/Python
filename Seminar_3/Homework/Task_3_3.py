# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def find_max_min_difference(list_without_int):
    min = list_without_int[0]
    max = list_without_int[0]
    for element in list_without_int:
        if element < min:
            min = element
        if element > max:
            max = element
    return max - min


def find_elements_without_int(list_of_numbers):
    list_without_int = []
    for element in list_of_numbers:
        if element % 1 != 0:
            list_without_int.append(element - int(element))
    return list_without_int


list_of_numbers = [float(element) for element in input(
    'Введите вещественные числа через пробел, для завершения ввода нажмите enter ').split()]
list_without_int = find_elements_without_int(list_of_numbers)
print(
    f'Pазница между максимальным и минимальным значением дробной части элементов введенного списка равна {find_max_min_difference(list_without_int)}')
