n = int(input())

arr=list(map(int,input().split()))

dp=[0]*n
dp[0] = arr[0]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+arr[i], dp[i])
        else :
            dp[i] = max(arr[i],dp[i])

print(max(dp))


# N = int(input())
# A = list(map(int, input().split()))
# d = [0] * N

# d[0] = A[0]

# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             d[i] = max(d[i],d[j]+A[i])
#         else:
#             d[i] = max(d[i],A[i])
# print(max(d))