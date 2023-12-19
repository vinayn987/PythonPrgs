print("Enter a string: ", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(f"{char} \t {ascii}")

""" 
There is another way to find ascii value
c = 'g'
print(f'The ASCII value of {c} is {ord(c)}')

"""