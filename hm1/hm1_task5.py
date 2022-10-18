# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

coor_a = []

for i in range(2):
    coor_a.append(int(input('enter a coords: ')))
coor_b = []

for i in range(2):
    coor_b.append(int(input('enter b coords: ')))

print(coor_a, coor_b)

distance = math.sqrt((coor_b[0] - coor_a[0]) ** 2 + (coor_b[1] - coor_a[1]) ** 2)
print()
print(f'distance between dots is {distance}')