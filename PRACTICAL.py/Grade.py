# Taking percentage as input and telling their grade 

# Let's take input from the user 
print("Please enter your percentage in your degree")
gpa = float(input("==> "))

# Test case by using nested if statement.

# Input is more than 80 then user got very good grade.
if gpa >= 81 and gpa < 100:
    print("Wow!! Congratulations You are very good at your studies.")

# Input is more than 60 and less than 80 then user got good grade.
elif gpa >= 61 and gpa < 80:
    print("Congratulations you are good at your studies, keep it up.")

# Input value is more than 40 and less than 60 then user got average grade.
elif gpa >= 41 and gpa < 60:
    print("Sorry, You are average in your studies. There is need of hardwork.")
# Input less than 40 then user was failed.
else:
    print("You are falied. Try again with best version of you.")