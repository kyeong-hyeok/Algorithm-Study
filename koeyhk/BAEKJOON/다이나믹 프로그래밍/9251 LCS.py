# 두 수열의 부분 수열 중 가장 긴 것 찾기
# 최대 1000글자
# 알파벳 대문자로만 이루어져 있음

# dp[i][j] = 문자열 a, b 각각의 i, j번째 글자까지의 최장 공통 부분 문자열 길이
# a[i] == b[j] -> 두 문자를 추가하기 전인 dp[i-1][j-1] + 1
# a[i] != b[j] -> dp[i-1][j], dp[i][j-1] 중 최댓값

import sys

input_data = sys.stdin.readline

a = list(input_data().rstrip())
b = list(input_data().rstrip())
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])