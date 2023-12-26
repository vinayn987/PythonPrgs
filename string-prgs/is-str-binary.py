# Check if a given string is binary or not 
import re

def is_binary_str(string):
    binary_ptn = r'^[01]+$'
    match = re.match(binary_ptn, string)
    
    return bool(match)

# Test the function

b_txt = "001101001"

result = is_binary_str(b_txt)

if result:
    print(f"{b_txt} is binary string")
else:
    print(f"{b_txt} is not binary string")
