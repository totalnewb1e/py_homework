# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

some_list = list(map(float, input('enter values divided by space and press enter: ').split()))
fp_list = []

print(some_list)

for i in range(len(some_list)):
    fp_list.append(some_list[i] - int(some_list[i]))
print(fp_list)

a = max(fp_list)
b = min(fp_list)

print(f'answer is {a - b}')