# 1로 시작, 1이 두 번 연속 x
# N = 90

# 처음 생각한 풀이
# 백트래킹 -> 시간 초과
# 백트래킹을 통해 이친수의 규칙 찾음 -> DP로 해결 가능!
# 1 -> 1
# 2 -> 10
# 3 -> 100 101
# 4 -> 1000 1001 1010
# 5 -> 10000 10100 10001 10010 10101

N = int(input())
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])


# 백트래킹 풀이 -> 시간 초과

N = int(input())
arr = []
result = 0


def bt():
    global result
    if len(arr) == N:
        result += 1
        return
    if len(arr) == 0:
        arr.append(1)
        bt()
        arr.pop()
    elif arr[-1] == 1:
        arr.append(0)
        bt()
        arr.pop()
    else:
        arr.append(0)
        bt()
        arr.pop()
        arr.append(1)
        bt()
        arr.pop()

bt()
print(result)