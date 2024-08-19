# 메모리 제한 4MB, 0.5초
# n개의 동전 = 100, 가치의 합 k원
# 사용하는 동전은 같지만 순서가 다른 것 -> 같은 경우

# 문제 접근 방법
# DP -> 동전을 사용하는 가지 수를 늘려가며 업데이트
# 동전별로 for문을 돌린다면 순서가 다른 것이 같은 것으로 취급되지 않는다!

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline

n, k = map(int, input_data().split())
coin = [int(input_data()) for _ in range(n)]
dp = [0] * 100001
dp[0] = 1

# c원 동전으로 i원 만들기 -> i-c원 + c원
for c in coin:
    for i in range(c, k+1):
        if i - c >= 0:
            dp[i] += dp[i-c]

print(dp[k])


# 처음 생각한 풀이 -> 백트래킹
# 메모리 초과, 시간 초과

# 문제의 메모리와 시간 제한에 맞지 않는 풀이이다.

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline

n, k = map(int, input_data().split())
coin = [int(input_data()) for _ in range(n)]
s = 0
result = 0
coin.sort()


def bt(x, s):
    global result
    if s >= k:
        if s == k:
            result += 1
        return
    for i in range(x, n):
        s += coin[i]
        bt(i, s)
        s -= coin[i]


bt(0, 0)
print(result)