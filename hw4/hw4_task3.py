# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

some_list = list(map(int, input('enter ur list divided by space: ').split()))

rez_list = []

# print(set(some_list)) вроде исходя из условия задания, это верное решение) вроде бы

for i in range(len(some_list)):
    if some_list.count(i) == True:
        rez_list.append(i)
print(rez_list)