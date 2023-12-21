def find_remainder(arr, length, modular):
    c = 1
    for i in range(length):
        c *= arr[i]
    return c % modular


arr = [10, 5, 14, 29]
length = len(arr)
modular = 9
print(find_remainder(arr, length, modular))