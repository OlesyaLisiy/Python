# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# с помощью математических формул нахождения корней квадратного уравнения
# с помощью дополнительных библиотек Python

a = -3
b = 2
c = 1

disc = b**2 - 4*a*c  # Дискриминант

if a == 0:
    x = -c / b
    print(x)
elif disc > 0:
    x1 = (-b - disc**0.5)/(2 * a)
    x2 = (-b + disc**0.5)/(2 * a)
    print(x1, x2)
elif not disc:
    x = -b/(2 * a)
    print(x)
else:
    print('Нет вещественных корней')


# A = int(input('Число А: '))
# B = int(input('Число B: '))
# C = int(input('Число C: '))
# D = B * B - 4 * A * C
# if D > 0:
#     x1 = ((-B) + D ** 0.5) / 2 * A
#     x2 = ((-B) - sqrt(D)) / 2 * A
#     print(round(x1, 3), round(x2, 3))
# elif D == 0:
#     x1 = (-B) / 2 * A
#     print(x1)
# else:
#     print('корней нет')