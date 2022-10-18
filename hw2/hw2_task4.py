# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ.
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

try:
    n = int(input('enter value for n to create a list from -n to n: '))
    rez = 1

    some_list = [*range(-n, n+1)]

    print(some_list)

    indexes_list = []

    for _ in range(5):
        indexes_list.append(int(input('enter position: ')))
    print(indexes_list)

    for i in indexes_list:
        rez *= some_list[i]

    print(f'answer is {rez}')
except:
    print('integer numbers only')