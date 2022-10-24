# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

input_number = int(input("Введите натуральное число "))
number = input_number
i = 2
my_list = []
while i <= number:
    if number % i == 0:
        my_list.append(i)
        number /= i
    else:
        i += 1
my_list = str(my_list).replace('[','').replace(']','')
print(f'Cписок простых множителей числа {input_number}: {my_list}')
