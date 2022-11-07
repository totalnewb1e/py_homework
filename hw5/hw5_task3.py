# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

my_line = open('RLE01.txt')

s = my_line.readline()
print(s)

def rle_encode(s):
    encoding = ''
    p_char = ''
    count = 1

    if not s: return ''

    for char in s:
        if char != p_char:
            if p_char:
                encoding += str(count) + p_char
            count = 1
            p_char = char
        else:
            count += 1
    else:
        encoding += str(count) + p_char
        return encoding


my_line.close()

print(rle_encode(s))

with open('RLE_encoded.txt', 'w') as encoded:
    encoded.write(rle_encode(s))
