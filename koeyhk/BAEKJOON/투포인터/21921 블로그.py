# N, X = 250,000
# O(N) -> 투 포인터 (슬라이딩 윈도우)
# l, l+X-1 -> l 증가하면서 비교

import sys

input_data = sys.stdin.readline

N, X = map(int, input_data().split())
visit = list(map(int, input_data().split()))
sum_x = sum(visit[:X])
result = sum_x
l = 0
period = 1
while l+X < N:
    sum_x = sum_x - visit[l] + visit[l+X]
    if result < sum_x:
        period = 1
        result = sum_x
    elif result == sum_x:
        period += 1
    l += 1

if result:
    print(result)
    print(period)
else:
    print("SAD")