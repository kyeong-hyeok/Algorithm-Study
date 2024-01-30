# N, K = 100,000
# O(N) -> 투포인터

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
num = list(map(int, input_data().split()))

l, r = 0, K-1
result = sum(num[0:K])
answer = result
for i in range(0, N-K):
    result = result - num[i] + num[i+K]
    answer = max(answer, result)