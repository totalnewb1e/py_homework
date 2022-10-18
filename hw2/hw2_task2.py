# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

try:
    n = int(input('enter value for n: '))
    div = 2

    while n % div != 0:
        div += 1

    print(f'least natural divisor except 1 is {div}')
except:
    print('integer numbers only')