number1 = 5
number2 = 10

sum = number1 + number2
print(f"The addition of {number1} and {number2} is {sum}")

print(type(number1))
print(isinstance(number1, int))

def sum(x, y):
    return x+y

add = sum(number1, number2)
print(type(add)) # Checking the data type
print(isinstance(add, int)) # checking the type of variable