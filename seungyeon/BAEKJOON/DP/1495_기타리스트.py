# # import sys
# # input=sys.stdin.readline

# # n,s,m=map(int,input().split(" "))
# # arr=list(map(int,input().split(" ")))

# # dp=[0] * (n)
# # dp[0] = s

# # for i in range(n):
# #     if dp[i] + arr[i] > m:
# #         if dp[i] - arr[i] < 0:
# #             print(-1)
# #             break
# #         dp[i] -= arr[i]
# #     else:
# #         dp[i] += arr[i]

# # print(dp)
# # print(dp[n-1])

# import sys
# input=sys.stdin.readline

# n,s,m=map(int,input().split(" "))
# arr=list(map(int,input().split(" ")))

# dp=[[0] * (m+1) for _ in range(n+1)]
# dp[0][s] = 1 # 0번째 곡 볼륨 s가 있다

# for i in range(n):
#     for j in range(m+1):

#         if dp[i][j] == 1:
#             min_val = j - arr[i]
#             max_val = j + arr[i]

#             if min_val >= 0:
#                 dp[i+1][min_val] = 1

#             if max_val <= m:
#                 dp[i+1][max_val] = 1

# result = -1

# for i in range(m,-1,-1):
#     if dp[n][i] == 1:
#         result = i
#         break

# print(result)



import sys
input=sys.stdin.readline

n,s,m=map(int,input().split(" "))
arr=list(map(int,input().split(" ")))


# i,j n개의 곡, 최대 m 볼륨 의 가능 유무
dp=[[False] * (m+1) for i in range(n+1) ]

dp[0][s] = True # 0번째 곡 볼륨 s 가능

v = s

for i in range(n):
    for j in range(m+1):

        if dp[i][j] :

            min_val = j - arr[i]
            max_val = j + arr[i]

            if min_val >= 0:
                dp[i+1][min_val] = True
            
            if max_val <= m :
                dp[i+1][max_val] = True

    
result = -1


for i in range(m,-1,-1):
    if dp[n][i] :
        result = i
        break
    
print(result)