a = input()
b = [int(i) for i in a]
count = [0] * 10
for i in b:
    count[i] += 1
for i in range(10):
    if count[i] > 0:
        print(i, count[i])