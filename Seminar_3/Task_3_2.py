# Задайте список. Напишите программу, которая определит,
# присутствует ли в данном списке строк некое число.

# my_list = ['123', '234', '12333', '567', '123']
# number = '123'
# nul = 0
# for elem in my_list:
#     if number in elem:
#         print(elem)
#         print(my_list.index(elem, nul))
#         nul = my_list.index(elem, nul) + 1


# my_list = ['123', '234', '12333', '567', '123']
# number = '123'
# for i, elem in enumerate(my_list):
#     if number in elem:
#         print(elem)
#         print(i)

arr = ['bbb21dd', 'Hello', 'World']
n = '21'
flag = False
for stroka in arr:
    if n in stroka:
        flag = True
        print('yes')
if flag == False:
    print('no')
