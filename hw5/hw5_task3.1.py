encoded_line = open('RLE_encoded.txt')

s = encoded_line.readline()
print(s)

def rle_decoding(s):
    decoding = ''
    count = ''

    for char in s:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = ''
    return decoding

encoded_line.close()

print(rle_decoding(s))

with open('RLE_decoded.txt', 'w') as decoded:
    decoded.write(rle_decoding(s))
