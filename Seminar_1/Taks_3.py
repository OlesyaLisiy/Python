# Для подготовки к экзамену Рон каждый день учит x заклинаний, а Гермиона на y заклинаний больше.
# Сколько заклинаний они выучат вместе через n дней.
# В первой строке вводится x – количество заклинаний, которые учит Рон.
# Во второй строке y – на сколько заклинаний больше учит Гермиона.

r = int(input('Введите сколько заклинаний учит Рон '))
h = int(input('Введите на сколько заклинаний больше учит Гермиона '))
n = int(input('Сколько дней Рон и Гермиона учат заклинания '))

print(f'За {n} дней Рон и Гермиона выучат {(r+(r+h))*n} заклинаний')
