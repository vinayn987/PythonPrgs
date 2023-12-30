# Creating calculator using match case statement

"""Creating a function 
calculator(parameter1, parameter2):

parameters: Get the input from the user and evaluate
             in the match case according to the selected
             choice
return: In match case there is number of cases in which 
        the selected case evaluate the values and 
        display the output


"""
def calculator(X, Y):

    choice = input("\nPlease select your operation '+\-\*\%\/\**\//' ==> ")
    match choice:
        case '+':
            print(f"{X} + {Y} = {(X+Y)}")
        case '-':
            print(f"{X} - {Y} = {(X-Y)}")
        case '*':
            print(f"{X} * {Y} = {(X*Y)}")
        case '/':
            print(f"{X} / {Y} = {(X/Y)}")
        case '%':
            print(f"{X} % {Y} = {(X%Y)}")
        case '**':
            print(f"{X} ^ {Y} = {(X**Y)}")
        case '//':
            print(f"{X} // {Y} = {(X//Y)}")
        case _ :
            print("Invalid choice")
                    

# Test case for the function
print("\nPlease enter two integer values to perform operations ")  
numberX = int(input("1st==> "))
numberY = int(input("2nd==> "))

calculator(numberX, numberY)