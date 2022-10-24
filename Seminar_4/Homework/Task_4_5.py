# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('file1.txt', 'r') as data1:
    polynomial_1 = str(data1.readline())
with open('file2.txt', 'r') as data2:
    polynomial_2 = str(data2.readline())
print(f"Первый многочлен: {polynomial_1}")
print(f"Второй многочлен: {polynomial_2}")


def find_polynomial_degree(polynomial):
    if 'x^' in polynomial:
        polynomial_degree_index = polynomial.find('^')
        degree = int(polynomial[polynomial_degree_index+1])
    elif ('x' in polynomial) and ('^' not in polynomial):
        degree = 1
    else:
        degree = -1
    return degree


def find_coeff(degree, polynomial):
    new_polynomial = polynomial.replace(' = 0', '')
    dict_with_coeff = {}
    if degree == 1:
        coeff_index = new_polynomial.find('*x')
        dict_with_coeff[0] = int(new_polynomial[coeff_index+4:])
        dict_with_coeff[1] = int(new_polynomial[:coeff_index])
    else:
        new_polynomial = polynomial.replace(' = 0', '')
        new_polynomial = new_polynomial.split(' + ')
        dict_with_coeff[0] = int(new_polynomial[-1])
        new_polynomial.pop(-1)
        k = 1
        for i in range(len(new_polynomial)-1, -1, -1):
            coeff_index = new_polynomial[i].find('*x')
            element_in_str = new_polynomial[i]
            element_in_num = int(element_in_str[:coeff_index])
            dict_with_coeff[k] = element_in_num
            k += 1
    return dict_with_coeff


def find_final_polynomial(degree, dic_result):
    result_str = ''
    if degree == 1:
        result_str = str(dic_result[0]) + '*x' + \
            ' + ' + str(dic_result[1]) + ' = 0'
    else:
        for i in range(len(dic_result)-2):
            result_str = str(dic_result[i+2]) + '*' + \
                'x^' + str(i+2) + ' + ' + result_str
        result_str += str(dic_result[1]) + '*x' + \
            ' + ' + str(dic_result[0]) + ' = 0'
    return result_str


degree_1 = find_polynomial_degree(polynomial_1)
degree_2 = find_polynomial_degree(polynomial_2)

dict_with_coeff_1 = find_coeff(degree_1, polynomial_1)
dict_with_coeff_2 = find_coeff(degree_2, polynomial_2)

# print(dict_with_coeff_1)
# print(dict_with_coeff_2)

dic_result = {}
for key, value in dict_with_coeff_1.items():
    dic_result[key] = value+dict_with_coeff_2[key]
# print(dic_result)

degree = max(degree_1, degree_2)

result_str = str(find_final_polynomial(degree, dic_result))
with open('file3.txt', 'w') as file:
    file.write(result_str)