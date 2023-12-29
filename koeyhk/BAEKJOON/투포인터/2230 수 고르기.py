# 투 포인터 - 배열에서 이중 for문으로 처리되는 작업을 2개 포인터의 움직임으로 O(N)에 해결하는 알고리즘

# N개의 정수로 이루어진 수열
# 두 수의 차이가 M 이상이며 제일 작은 경우 구하기
# N = 100,000  M = 2,000,000,000
# O(N)으로 수행해야함 -> 이중 for 문 x

# 놓친 부분 - r의 초기값
# 1. 이분탐색처럼 l과 r의 초기값을 각각 0, N-1로 설정했지만 초기값은 둘다 0이어야 함
# ** 직접 예시를 통해 문제 파악하는 것이 중요 **

import sys

input_data = sys.stdin.readline
N, M = map(int, input_data().split())
num = [int(input_data()) for _ in range(N)]
num.sort()
l, r = 0, 0
min_d = 20000000000

while l <= r < N:
    sub = num[r] - num[l]
    if M < sub:
        if sub < min_d:
            min_d = sub
        l += 1
    elif sub == M:
        min_d = M
        break
    else:
        r += 1

print(min_d)