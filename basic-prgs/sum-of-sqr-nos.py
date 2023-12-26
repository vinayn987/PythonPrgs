def square_sum(n):
    sm = 0
    for i in range(1, n+1):
        sm += pow(i, 2) # for cube square we use sm += pow(i, 3) that's it
    return sm           # and remain everything same..


n = 4
print(f"{square_sum(n)}")