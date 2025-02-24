import sys
input=sys.stdin.readline

n=int(input())

arr=[]
arr.append((1,1,1,1))
for i in range(1,n+1):
    a,b,c=map(int,input().split(" "))
    arr.append((i,a,b,c))

dp=[0]*(n+1)

arr.sort(key=lambda x:x[3])

for i in range(1,n+1):
    for j in range(0,i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i],dp[j]+arr[i][2])

max_height=max(dp)


index=n
answer =[]

while index != 0:
    if dp[index] == max_height:
        answer.append(arr[index][0])
        max_height-=arr[index][2]
    index -= 1

print(len(answer))
answer.reverse()

for i in answer:
    print(i)



# dp=[0] * (n+1)

# arr.sort(key=lambda x:x[1]) # 넓이 순 정렬

# for i in range(1,n+1):
#     for j in range(0,i):
#         if arr[i][3] > arr[j][3]:
#             dp[i] = max(dp[i],dp[j]+arr[i][2])

# max_height = max(dp)

# index = n
# history=[]

# while index != 0:
#     if dp[index] == max_height:
#         history.append(arr[index][0])
#         max_height-=arr[index][2]

#     index -= 1

# history.reverse()
# print(len(history))
# for i in history:
#     print(i)