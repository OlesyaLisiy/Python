# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def list_creation():
    list_of_numbers = []
    list_of_elements = [element for element in input(
        'Введите числа через пробел, для завершения ввода нажмите enter ').split()]
    for element in list_of_elements:
        list_of_numbers.append(int(element))
    return list_of_numbers


def sum_of_elements_on_odd_positions(list_of_numbers):
    my_sum = 0
    for index in range(len(list_of_numbers)):
        if index % 2 != 0:
            my_sum = my_sum + list_of_numbers[index]
    return my_sum


print(sum_of_elements_on_odd_positions(list_creation()))
