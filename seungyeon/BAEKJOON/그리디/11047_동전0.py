# # n,k=map(int,input().split())
# # coins = []
# # for i in range(n):
# #     coins.append(int(input()))

# # cnt = 0
# # for i in range(n-1,-1,-1):
    
# #     if coins[i] <= k :
# #         cnt += k // coins[i]
# #         k = k % coins[i]

# # print(cnt)

# import sys
# input=sys.stdin.readline

# n,k=map(int,input().split(" "))
# arr =[]
# for i in range(n):
#     arr.append(int(input()))

# cnt = 0

# for i in range(n-1,-1,-1):
#     if k // arr[i] > 0:
#         cnt += k // arr[i]
#         k %= arr[i]

# print(cnt)

import sys
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[int(input().strip()) for i in range(n)]

arr2 = sorted(arr,reverse=True)

cnt = 0

for i in range(n):

    h = k // arr2[i]
    cnt += h

    if k >= arr2[i] and k % arr2[i] == 0: 
        print(cnt)
        exit()
    
    elif k >= arr2[i] and k % arr2[i] != 0:
        k -= arr2[i] * h

    else :
        continue

