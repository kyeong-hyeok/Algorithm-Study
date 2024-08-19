import sys
from math import gcd

input_data = sys.stdin.readline

N = int(input_data())
co = [int(input_data()) for _ in range(N)]

div = []
for i in range(N-1):
    div.append(co[i+1]-co[i])

g = div[0]
for d in div:
    g = gcd(g, d)

result = 0
for d in div:
    result += d // g - 1

print(result)