rounds = int(input())
mishka = 0
chris = 0
for i in range(rounds):
    a,b = map(int,input().split())
    if a > b:
        mishka += 1
    elif a < b:
        chris += 1
if mishka > chris:
    print('Mishka')
elif mishka < chris:
    print('Chris')
else:
    print('Friendship is magic!^^')