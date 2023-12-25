#Convert snake_case to PascleCase

age = "what_is_your_age?"

res = age.replace("_", " ").title().replace(" ", " ")
print(str(res))