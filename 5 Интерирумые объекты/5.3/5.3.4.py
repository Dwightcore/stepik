a = input().lower()
b = 0
for i in range(len(a)):
    if a.count(a[i]) > b:
        b = a.count(a[i])
print(b)