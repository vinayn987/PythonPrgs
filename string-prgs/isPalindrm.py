def isPalidrome(s):
    return s == s[::-1]

s = "12211221" # racecar, level, radar, mam are polindrome strings
#s = str(n)
half = int(len(s)/ 2)
_1st_str = s[:half]
_2nd_str = s[half:]
res = isPalidrome(s)

print("Palindrome", res if res == True else False)

print("Symmetrical ", True if _1st_str == _2nd_str else False)
print(half)