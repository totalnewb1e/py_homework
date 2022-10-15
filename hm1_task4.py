# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

try:
    sector = int(input('enter sector from 1 to 4: '))

    if sector == 1:
        print('x >=0 , y >= 0')
    elif sector == 2:
        print('x <=0 , y >= 0')
    elif sector == 3:
        print('x <=0 , y <= 0')
    elif sector == 4:
        print('x <=0 , y <= 0')
    else:
        print(' error ')
except:
    print('nums from 1 to 4')