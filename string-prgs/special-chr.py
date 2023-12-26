# Check if a string contains any special characters
import re 

def find_special_char(input):
    ptn = r'[^a-zA-Z0-9_]'
    special_char = re.findall(ptn, input)
    if special_char:
        print(f"Special chars found:{','.join(set(special_char))}")
    else:
        print("No special chars found.")
# Test the function
        
input = "Hello!@#$%^&*"

find_special_char(input)
