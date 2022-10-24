# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


coeff = int(
    input("Введите натуральное число, которое будет задавать степень многочлена "))
new_list = []
for i in range(coeff + 1):
    new_list.append(randint(0, 101))

result_str = ''
if coeff == 1:
    result_str = str(new_list[0]) + '*x' + ' + ' + str(new_list[1]) + ' = 0'
else:
    for i in range(len(new_list)-2):
        result_str = str(new_list[i+2]) + '*' + 'x^' + str(i+2) + ' + ' + result_str 
    result_str += str(new_list[1]) + '*x' + ' + ' + str(new_list[0]) + ' = 0'
print(result_str)
