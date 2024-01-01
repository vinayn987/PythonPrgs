class BikeShop:
   
    stock = 100
    def available_bikes(self):
        return self.stock
    
    def bike_for_rent(self, bike):
        if bike > self.stock:
            print("Sorry we don't have that much stock ")
        if bike <=0:
            print("Please enter required bikes more than 0")
        else:
            print(f"The total rent price of bikes is {(bike*100)}")
            print(f"Total bikes {(self.stock - bike)}")
            print("Thank you for coming Visit again")

res = BikeShop()

print('''
    A.Availble stock
    B.Bikes for rent 
    C.exit

''')
while True:
    order = input("Please enter your choice A\B\C ==> ")
    match order:
        case "A":
            print(res.available_bikes())

        case "B":
            print("     Please enter number of bikes")
            bike = int(input("===> "))
            res.bike_for_rent(bike)
        case "C":
            print(exit())
        
        case _:
            print("Invalid choice")