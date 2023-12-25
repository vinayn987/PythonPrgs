# Python code to check a string which contains all vowels
import re

def contains_vowels(name):
    vowel_ptn = re.compile("[aeiouAEIOU]")
    match = vowel_ptn.search(name)

    return (True if match else False)
# test the function
name = "My name is Tanmay"

if contains_vowels(name):
    print("The string contain vowels")
else:
    print("The string does not contain vowels")
