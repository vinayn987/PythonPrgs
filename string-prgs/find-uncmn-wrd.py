# Find uncommon words between two strings

import re 

def find_uncommon_words(str1, str2):
    word1 = set(re.findall(r'\b\w+\b', str1.lower()))
    word2 = set(re.findall(r'\b\w+\b', str2.lower()))

    uncommon_words = word1.symmetric_difference(word2)

    return uncommon_words
# Test the function
txt1 = "Python is easy to code"
txt2 = "Python is free and open-source"
result = find_uncommon_words(txt1, txt2)

print(f"uncommon words : {result}")