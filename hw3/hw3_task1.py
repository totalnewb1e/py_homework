# Напишите программу, которая найдёт произведение пар чисел списка.

some_list = list(map(int, input('enter values divided by space and press enter: ').split()))
rez_list = []

print(some_list)

for i in range((len(some_list) + 1) // 2):
    rez_list.append(some_list[i] * some_list[- 1 - i])

print(rez_list)