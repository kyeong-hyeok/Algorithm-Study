import sys
import math

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
color = [0]*N
for i in range(M):
    l, r = map(int, input_data().split())
    for j in range(l-1, r):
        color[j] = i+1

count = 0
for i in range(len(color)-1):
    if color[i] != 0 and color[i] != color[i+1]:
        count += 1
if color[-1] != 0:
    count += 1
print(int(math.pow(2, count)))