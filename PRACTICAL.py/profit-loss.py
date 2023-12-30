# Checking whether a man got profit or not 
print("Please enter the selling price of the product")
selling_price = int(input("==> "))
print()
print("Please enter the actual cost of the product")
actual_cost = int(input("==> "))
# Test case by using nested if statement
if selling_price >  actual_cost:
    profit = selling_price - actual_cost
    print(f"Congrats you made profit of {profit} rupees.")
elif selling_price < actual_cost:
    loss = actual_cost - selling_price
    print(f"Sorry! You made incurred loss of {loss} rupees.")
else:
    print("You haven't made either a profit or a loss.")
