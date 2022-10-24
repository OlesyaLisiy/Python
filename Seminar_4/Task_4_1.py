# Задайте строку из набора чисел. Напишите программу,
# которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# 1
str = '11 27 73 40 35 76'
result = list(map(int, (str.split())))
print(max(result), min(result))


# 2
nums = '11 27 73 40 35 76'
my_list = [int(num) for num in nums.split()]
print(max(my_list), min(my_list))

# 3
stroka = '3, 4, 5, 6'
x = stroka.split(', ')
for i in range(len(x)):
    x[i] = int(x[i])
max_list = x[0]
min_list = x[0]
for i in x:
    if max_list < i:
        max_list = i
    if min_list > i:
        min_list = i
print(max_list, min_list)