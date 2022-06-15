import math
L,W,H = map(int,input().split())
a = (2 * (L + W)) * H / 16
print(math.ceil (a))