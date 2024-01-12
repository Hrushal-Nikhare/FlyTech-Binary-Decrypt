input_string = input("Enter a string to encode: ")
# input_string = "The fly runs at midnight."
size = int(input("Enter the size of each split: "))
# size = 7
flip_bit = abs(int(input("Enter the bit to flip from the back: ")))*-1
# flip_bit = -4
ascii_values = [ord(char) for char in input_string]

split = [bin(value)[2:] for value in ascii_values]

for i in range(len(split)):
    # flip the bit
    if split[i][flip_bit] == '0':
        split[i] = split[i][:flip_bit] + '1' + split[i][flip_bit+1:]
    else:
        split[i] = split[i][:flip_bit] + '0' + split[i][flip_bit+1:]

if len(split) % size != 0:
    for i in range(len(split)):
        split[i] = "0"*(size-len(split[i])) + split[i]

# print the encoded string
encoded = f"{size}~{abs(flip_bit)}_" + ''.join(split)
print(encoded)
