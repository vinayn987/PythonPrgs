# check if a string has entered substring
import re

str = "Geek means a knowledgable person"

print(True if re.search("a", str) else False)