def prime(start, end):
    lst = []
    flag = 0
    for i in range(start, end):
        for j in range(2, i):
            if (i%j == 0):
                flag = 1
                break
            else:
                flag = 0
        if (flag == 0):
            lst.append(i)
    return lst

start = 2
end = 11

lst = prime(start, end)
if len(lst) == 0:
    print("The are no prime numbers in this range")
else:
    print(f"The prime numbers in this range are {lst}")
    