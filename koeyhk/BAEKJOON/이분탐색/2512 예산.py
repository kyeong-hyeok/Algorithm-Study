# 요청 다 되면 -> 그대로 배정
# 요청 다 되지 않으면 -> 특정한 정수 상한액 계산 그 이상인 요청에는 상한액 배정
# N = 10,000
# 이분탐색 -> O(logN) * O(N)

import sys

input_data = sys.stdin.readline

N = int(input_data())
budget = list(map(int, input_data().split()))
M = int(input_data())


def check(x):
    result = 0
    for b in budget:
        if b <= x:
            result += b
        else:
            result += x
    return result


l, r = 0, max(budget)
while l <= r:
    m = (l+r) // 2
    k = check(m)
    if k <= M:
        l = m + 1
    else:
        r = m - 1

print(r)
