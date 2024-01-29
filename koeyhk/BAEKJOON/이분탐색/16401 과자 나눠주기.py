# M, N = 1,000,000
# O(M) * O(N) -> 시간 초과
# O(N) (해당 길이로 나누어 줄 수 있는 사람의 수) * (길이 찾기 -> 이분 탐색)

import sys

input_data = sys.stdin.readline

M, N = map(int, input_data().split())
snack = list(map(int, input_data().split()))
l, r = 1, max(snack)
snack.sort(reverse=True)


def divide(x):      # O(N) = O(1,000,000)
    result = 0
    for i in range(N):
        s = snack[i] // x
        if s == 0:
            break
        result += s
    return result


answer = 0
while l <= r:       # O(log(max(L))) = O(log 1,000,000,000)
    m = (l+r) // 2
    k = divide(m)
    if k >= M:
        l = m + 1
    else:
        r = m - 1

print(r)