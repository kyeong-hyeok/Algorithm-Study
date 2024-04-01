import sys

input=sys.stdin.readline
N,k=map(int,input().split())

arr=list(map(int,input().split()))
answer = 0
visited=[0]*N

def find(x,n):
    global answer

    if x < 500:
        return 
    if n == N:
        answer += 1
        return
    
    x -= k
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(x+arr[i],n+1)
            visited[i] = 0

find(500,0)
print(answer)

# for kit in permutations(arr,n):
#     total = 500
#     for i in kit:
#         total -= k # 매일 감소
#         if total + i < 500: 
#             total += k
#             break
#         total += i

#         print(kit,i,total)
#         answer += 1
#     # if total >= 500:
#     #     print(kit,i,total)
#     #     answer += 1

# print(answer//n)