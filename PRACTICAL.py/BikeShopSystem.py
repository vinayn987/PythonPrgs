# Creating a bike shop system using oop's concepts
class BikeShop:
    #Creating a class variable
    stock = 100
    def available_bikes(self):
        return self.stock # accessing and returning a class variable by default(self)  parameter
    
    # function for rent logic
    def bike_for_rent(self, bike):
        if bike > self.stock:
            print("Sorry we don't have that much stock ")
        if bike <=0:
            print("Please enter required bikes more than 0")
        else:
            print(f"The total rent price of bikes is {(bike*100)}")
            print(f"Total bikes {(self.stock - bike)}")
            print("Thank you for coming Visit again")

res = BikeShop() # creating an object 

# Testing the class BikeShop
print('''
    A.Availble stock        
    B.Bikes for rent 
    C.exit

''')        # Note: don't print the function which printing itself 
            # because it shows None value 
            # If you write a return function then call the function in print()
while True:
    order = input("Please enter your choice A\B\C ==> ")
    match order:
        case "A":
            print(res.available_bikes()) # calling the function

        case "B":
            print("     Please enter number of bikes")
            bike = int(input("===> "))
            res.bike_for_rent(bike) # calling the function
        case "C":
            print(exit())
        
        case _:
            print("Invalid choice")