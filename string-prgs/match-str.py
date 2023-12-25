# Python code to count the number of matching characters in a pair of string

import re

def count_match(str1, str2):
    common_char = re.compile('[%s]' % re.escape(' '.join(set(str1) & set(str2))))

    match_str1 = common_char.findall(str1)
    match_str2 = common_char.findall(str2)

    return len(match_str1), match_str1, len(match_str2), match_str2
# test the function with some example

string1 = "hello"
string2 = "world"

count1, result1, count2, result2 = count_match(string1, string2)

print(f"Number of matching characters in first string {count1}")
print(f"Matching characters {result1}")
print(f"Number of matching characters in second string {count2}")
print(f"The matching characters {result2}")
