def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] >= max:
            max = arr[i]
    return max

size = int(input("size:"))
array = [int(input()) for _ in range(size)]
n = len(array)
print(f"{largest(array, n)} is the largest.")