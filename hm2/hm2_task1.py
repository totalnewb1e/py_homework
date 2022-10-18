# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

try:
    n = int(input('enter ur number: '))
    curr = 1

    for i in range(1, n+1):
        curr *= i
        print(curr, end=' ')
    print()
    print(f'fac of {n} is {curr}')
except:
    print('integer numbers only')
