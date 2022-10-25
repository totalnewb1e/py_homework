# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('enter n: '))

multipliers = []

a = 2

while n > 1:
    if n % a == 0:
        multipliers.append(a)
        n /= a
    else:
        a += 1
print(multipliers)
