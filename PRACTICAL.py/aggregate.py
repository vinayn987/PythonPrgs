class Customer:

    def __init__(self, name, gender, address):
        self.name = name 
        self.gender = gender
        self.address = address

class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

add = Address("Vijayapura", 210003, "KA")
cust = Customer("Vinay", "Male", add)
"""
Here, Address class's  object(add) is has sent in Customer class as a value 
arguement by this technique we can access the one class data to another data
is called Aggregation

"""
print(cust.address.pin)
# output: 210003
