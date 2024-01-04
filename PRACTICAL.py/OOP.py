class Bike:
    stock = 100
    
    def __init__(self):
        self.bikes = Bike.stock
    @staticmethod 
    def get_bikes(req):
        print(f"{req} is your need.")
    @staticmethod
    def give_stock(req):
        avail =  Bike.stock - req
        print(f"{avail} is the remain Bike stock")
        
obj = Bike()
need = int(input("Enter the Stock need: "))

obj.get_bikes(need)
obj.give_stock(need)