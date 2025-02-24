import sys
input=sys.stdin.readline


# 길이가 n인 이진수열의 개수
# 1 또는 00 만 가능

# 1 과 00 으로 n칸수를 채워야함

n = int(input())

if n == 1:
    print(1)
    exit()
    
dp = [0]*(n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])