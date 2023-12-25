test_str = "GeeksforGeeks"
res = max(test_str, key=lambda x: test_str.count(x))
print(res)
