# 인출하는 데 필요한 시간이 적은 순으로 정렬 -> 최솟값

import sys

input_data = sys.stdin.readline

N = int(input_data())
P = list(map(int, input_data().split()))
P.sort()
prev, result = 0, 0
for i in range(N):
    prev += P[i]
    result += prev
print(result)