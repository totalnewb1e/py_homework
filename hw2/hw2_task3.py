# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

try:
    n = int(input('enter value for n: '))
    sum = 0

    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    print(f'sum of positive nums in range from 1 to {n} is {sum}')
except:
    print('integer numbers only')