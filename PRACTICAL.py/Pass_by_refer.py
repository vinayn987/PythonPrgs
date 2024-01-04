# Example for pass by value
class Customer:

    def __init__(self, name): # In python everything is object
        self.name = name # declare the variable by self object 
        print(self.name) # self is default an object in python

def greet(customer): # passing the address of the name variable
    print(customer.name) # accessing the name value by using dot operator

cust = Customer("Ravi") # Giving the value as arguement
greet(cust) # passign the reference variable as arguement

print(cust.name) # printing the value of name using its reference variable 
