# Remove all duplicates from a string 
import re

test = "moountaain"

modify = re.sub(r'(.)\1+', r'\1', test)

print(f"Modified string {modify}")
