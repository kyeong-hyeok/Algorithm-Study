# n,k=map(int,input().split())
# coins = []
# for i in range(n):
#     coins.append(int(input()))

# cnt = 0
# for i in range(n-1,-1,-1):
    
#     if coins[i] <= k :
#         cnt += k // coins[i]
#         k = k % coins[i]

# print(cnt)

import sys
input=sys.stdin.readline

n,k=map(int,input().split(" "))
arr =[]
for i in range(n):
    arr.append(int(input()))

cnt = 0

for i in range(n-1,-1,-1):
    if k // arr[i] > 0:
        cnt += k // arr[i]
        k %= arr[i]

print(cnt)