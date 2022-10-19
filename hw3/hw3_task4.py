# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке

f = int(input('enter value for fib number: '))

fib1 = fib2 = 1

print(f'fib line for {f} is')
print(fib1, fib2, end=' ')

for i in range(2, f):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

