test_str = "GeeksforGeeks"
res = min(test_str, key=lambda x: test_str.count(x))
print(res)
