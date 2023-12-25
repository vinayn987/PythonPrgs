# Find the word frequency in the string shorthands

man = "A man is homo sapien, it means he is human being"
freq = {key: man.count(key) for key in man.split()}

print(f"The word frequency {freq}")
