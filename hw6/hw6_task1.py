# Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.

etr_list = list(map(int, input('enter any digits: ').split()))

filtered_list = list(filter(lambda x: x>9 and x<100, etr_list))

test_list = [i for i in etr_list if i>9 and i<100]

print(*filtered_list)
print(*test_list)