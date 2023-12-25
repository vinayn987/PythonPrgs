# Python code to find minimum  frequent(repeated) word

txt = "geeksforgeeks"

min_chr = min(txt, key = lambda x : txt.count(x))

print(f"The least frequent character is {min_chr}")

