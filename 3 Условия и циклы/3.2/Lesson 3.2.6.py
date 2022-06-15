# put your python code here
s, v1, v2, t1, t2 = map(int,input().split())

player1 = s * v1 + 2 * t1
player2 = s * v2 + 2 * t2
if player1 < player2:
    print('First')
else:
    if player1 > player2:
        print('Second')
    else:
        print('Friendship')