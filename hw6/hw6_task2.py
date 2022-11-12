# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

some_list = [12, 'sadf', 5643]

num_list = list(filter(lambda x: x if type(x) == int else None, some_list))
alpha_list = list(filter(lambda x: x if type(x) == str else None, some_list))

num_list1 = [i for i in some_list if type(i) == int]
alpha_list1 = [i for i in some_list if type(i) == str]

print(alpha_list, num_list)
print(alpha_list1, num_list1)
