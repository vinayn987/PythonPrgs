def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for i in num_str:
        sum += int (i) ** n
    if sum == num:
        return True
    else:
        return False
    
num = 153
print(f"{is_armstrong(num)}")