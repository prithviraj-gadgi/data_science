l = [('Bob', 20), ('Alice', 30), ('Alice', 10)]

l.sort(key=lambda x: (x[0]))

print(l)