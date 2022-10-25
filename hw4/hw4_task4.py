# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

from random import randint
import itertools

k = int(input('enter power for polynomial: '))

while k <= 0:
    k = int(input('error. try positive number or not zero: '))

r = [randint(1, 100) for i in range(k + 1)]
print(f'list of coefs is {r}')

def get_poly(k, r):
    giglet = ['x^']*(k-1) + ['x']
    rez = [[a, b, c] for a, b, c in itertools.zip_longest(r, giglet, range(k, 1, -1), fillvalue='')]
    for i in rez:
        i.append(' + ')
    rez = list(itertools.chain(*rez))
    rez[-1] = ' = 0'
    return ''.join(map(str, rez))

poly1 = get_poly(k, r)
print(poly1)

with open('poly1.txt', 'w') as p1:
    p1.write(poly1)
