a = [10, 12, 14, 11, 13, 16]
b = []
for i in range(0, len(a), 2):
    b.append(a[i] + a[i + 1])
print(b)
