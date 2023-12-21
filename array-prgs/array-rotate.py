def rotateList(arr, d, n):
    arr[:] = arr[d:n] + arr[0:d]
    return arr

arr = [1, 2, 3, 4]
rotatnum = 1
n = len(arr)
print(rotateList(arr, rotatnum, n))
