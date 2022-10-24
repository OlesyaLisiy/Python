# Напишите программу, которая определит позицию второго
# вхождения строки в списке, либо сообщит, что ее нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


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


# my_list = ['123', '234', '12333', '567', '123']
# number = my_list[0]
# print(my_list.index(number, 1))

list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
string = input('введите строку: ')
count = 0
i = 0
flag = True
while i < len(list_1) and flag:
    if string == list_1[i]:
        count += 1
        if count == 2:
            flag = False
            print(i)
    i += 1

if flag:
    print(-1)