
# Delete a letter from a string in python

def remove_char(s, i):
    bit = bytearray(s, 'utf-8')
    del bit[i]
    return bit.decode()

s = "hello world"
i = 4
str = remove_char(s, i)
print(str)