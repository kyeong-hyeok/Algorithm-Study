# n = int(input())

# # DP 테이블 초기화
# d = [0] * 1000001

# # 2부터 n까지 거꾸로 올라가기
# # d[i]는 숫자 i가 1이 되는데 걸리는 최소한의 연산 횟수
# for i in range(2, n+1):

#     # 1을 빼는 경우 
#     # d[i-1] (i-1이 1이 되는데 필요한 최소한의 연산) + 1 (i에서 1을 빼서 i-1이 되는데 필요한 연산 횟수 1회)
#     d[i] = d[i-1] + 1 

#     # i를 2로 나눈 값이 1이 되는데 걸리는 최소 연산 횟수 + i를 2로나누는 연산횟수 1회
#     if i%2 == 0:
#         d[i] = min(d[i], d[i//2] + 1) # 2로 나누는게 적은지 1 빼는게 적은지
#     if i%3 == 0:
#         d[i] = min(d[i], d[i//3] + 1)

# # 결과 출력
# print(d[n])

n = int(input())

dp=[0 for i in range(n+1)]


for i in range(2,n+1):
    dp[i] = dp[i-1] + 1

    if  i % 2 == 0:

        dp[i] = min(dp[i], dp[i//2] + 1)

    if  i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)


print(dp[n])