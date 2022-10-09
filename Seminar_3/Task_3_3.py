# Напишите программу, которая определит позицию второго
# вхождения строки в списке, либо сообщит, что ее нет.

# my_list = ['123', '234', '12333', '567', '123']
# number = my_list[0]
# for i, elem in enumerate(my_list):
#     if number == elem and i != 0:
#         print(elem)
#         print(i)


# my_list = ['123', '234', '12333', '567', '123']
# number = my_list[0]
# for i in range(1, len(my_list)):
#     if number == my_list[i]:
#         print(i)


my_list = ['123', '234', '12333', '567', '123']
number = my_list[0]
print(my_list.index(number, 1))