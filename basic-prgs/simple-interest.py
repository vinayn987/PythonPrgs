def simple_interest(p, t, r):
    si = (p*t*r)/100
    return si


p = 5
t = 3
r = 8

print(f"The simple interest is {simple_interest(p, t, r)}")