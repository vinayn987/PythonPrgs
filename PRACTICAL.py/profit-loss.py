# Checking whether a man got profit or not 
print("Please enter the selling price of the product")
selling_price = int(input("==> "))
print()
print("Please enter the actual cost of the product")
actual_cost = int(input("==> "))
# Test case by using nested if statement

# checking for profit in if condition
if selling_price >  actual_cost:
    profit = selling_price - actual_cost
    print(f"Congrats you made profit of {profit} rupees.")

# checking for loss in elif condition
elif selling_price < actual_cost:
    loss = actual_cost - selling_price
    print(f"Sorry! You made incurred loss of {loss} rupees.")
    
# checking for no change in else part
else:
    print("You haven't made either a profit or a loss.")
