# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('enter value for n: '))
d = n

b: str = ''

while d > 0:
    b = str(d % 2) + b
    d = d // 2

print(f'decimal {n} is binary {b}')