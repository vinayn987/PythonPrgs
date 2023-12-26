f3 = 0
f1 = 1
f2 = 1
n = 5

if n == 0 or n == 1:
    print(f"{n} is a fibonacci number")

else:
    while f3 < n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    if f3 == n:
        print(f"{n} is a fibonacci number")
    else:
        print(f"{n} is not a fibonacci number")
