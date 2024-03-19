# N, M = 100,000
# O(N^2) 미만

import sys

input_data = sys.stdin.readline
N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
s = [0]
result = 0
for n in num:   # O(N)
    result += n
    s.append(result)
for _ in range(M):      # O(N+M)
    i, j = map(int, input_data().split())
    print(s[j]-s[i-1])