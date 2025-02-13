# # 마지막 계단을 밟아야한다 
# # 2칸 전 + 1칸전 
# # 총 점수의 최댓값

# import sys
# input=sys.stdin.readline

# n = int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))

# dp=[0 for _ in range(n)]


# if n < 2:
#     print(sum(arr))
# else:
#     dp[0] = arr[0]
#     dp[1] = arr[0] + arr[1]

#     for j in range(2,n):
#         dp[j] = max(dp[j-2]+arr[j], dp[j-3]+arr[j-1]+ arr[j])

#     print(dp[-1])


# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=[ int(input().strip() ) for i in range(n)]


# dp=[0 for _ in range(n)]
# # 계단은 한개씩 또는 두개씩
# # 연속된 3개는 못밟음
# # 마지막은 무조건 밟음

# # 0 안밟음, 1밟음


# dp[0][0] = 0
# dp[0][1] = arr[0]

# dp[1][0] = dp[0][1]
# dp[1][1] = dp[0][1] + arr[1]

# dp[2][0] = max(dp[1][0], dp[1][1])
# dp[2][1] = max(dp[1][0], dp[1][1]) + arr[2]

# for i in range(3,n):
#     dp[i-1][1] = max(dp[i-2][1], dp[i-1][1]) + arr[i-1]
    
# # dp[n-1][1] = max(dp[n-1-2][1]+1, dp[n-1-1][1],dp[n-1-3][1], dp[n-1-1][0],dp[n-1-2][0]) + arr[n-1]

# print(dp)

# print(dp[n-1][1])

# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=[ int(input().strip() ) for i in range(n)]

# dp=[0 for _ in range(n)]


# if n < 2:
#     print(sum(arr))
# else:
#     dp[0] = arr[0]
#     dp[1] = arr[0]+arr[1]

#     for i in range(2,n):
#         dp[i] = max(arr[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
#         # 두칸전 + 지금 , 3칸전 + 한칸전 + 지금금

#     print(dp[-1])



import sys
input=sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

dp=[0 for _ in range(n)]

if n < 2:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]


    for i in range(2,n):
        # 1,2개 전을 안밟고 3개전을 밟거나, 1,2개 전을 밟거나나
        dp[i] = max(dp[i-2]+arr[i] , dp[i-3]+arr[i-1] + arr[i])

    print(dp[-1])