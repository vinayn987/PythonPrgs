def compound_interest(principal, time, rate):
    amount = principal*(pow((1 + rate/100), time))
    CI = amount - principal
    return CI


principal = 1000
rate = 8
time = 3

ci = compound_interest(principal, time, rate)
print(f"The compound interest is {round(ci, 2)}")
