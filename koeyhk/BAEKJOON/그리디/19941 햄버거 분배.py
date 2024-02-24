# N = 20,000 K = 10
# 제일 앞에 있는 햄버거 먹는 게 최대 -> i-K ~ i+K까지 순차적으로 확인
# O(NK)

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
loc = list(input_data().rstrip())
result = 0
for i in range(N):
    if loc[i] == 'P':
        for j in range(i-K, i+K+1):
            if 0 <= j < N and loc[j] == 'H':
                loc[j] = 0
                result += 1
                break
print(result)