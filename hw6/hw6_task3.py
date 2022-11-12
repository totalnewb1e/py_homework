# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

try:
    n = input('enter ur n: ')

    print(sum(map(float, n.replace('.', '').replace('-', ''))))
except:
    print('try real numbers')

# def f(n):
#     sum = 0
#     for i in str(n):
#         if i != '.':
#             sum += int(i)
#     return sum
#
# print(f(n))
