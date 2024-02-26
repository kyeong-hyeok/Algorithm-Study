# N, M = 200,000
# 최대 10개의 키워드 -> 메모장에 있었다면 지우기
# 해시, 집합

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
memo = set(input_data().rstrip() for _ in range(N))
result = N
for _ in range(M):
    word = list(input_data().rstrip().split(','))
    for w in word:
        if w in memo:
            memo.remove(w)
            result -= 1
    print(result)