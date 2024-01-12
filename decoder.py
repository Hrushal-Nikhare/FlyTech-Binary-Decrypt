import textwrap

# 7~4_1011100110000011011010101000
# 1101110110010011100010101000
# 1111010111110111001101111011
# 0101000110100111111000101000
# 1100101110000111011001100110
# 1100001110111111000001111100
# 0100110

# Functions
def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])


# Setting Variables
# binary = input('binary string: ')
binary = '7~4_1011100110000011011010101000110111011001001110001010100011110101111101110011011110110101000110100111111000101000110010111000011101100110011011000011101111110000011111000100110'
binary = binary.split('_')
binary[0] = binary[0].split('~')

size = int(binary[0][0])
flip_bit = int(binary[0][1]) * -1 # bit to be flipped from the back
actual = binary[1]

# split the binary by size
split = textwrap.wrap(actual,size)

# reverse encoding
for i in range(len(split)):
    # flip the bit
    if split[i][flip_bit] == '0':
        split[i] = split[i][:flip_bit] + '1' + split[i][flip_bit+1:]
    else:
        split[i] = split[i][:flip_bit] + '0' + split[i][flip_bit+1:]
    
    # add leading zeros
    split[i] = "0"*(8-size) + split[i]

# print the decoded string
print(binary_to_string(split))
# or the unreadable one-liner version
# print(''.join([chr(int(i, 2)) for i in split]))
