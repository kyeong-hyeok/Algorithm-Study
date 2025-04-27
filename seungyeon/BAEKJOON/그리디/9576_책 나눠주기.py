# import sys
# t=int(input())
# for _ in range(t):
#     n,m=map(int,input().split())

#     visited=[False]*n
#     arr=[[] for _ in range(n)]
#     for i in range(m):
#         a,b=map(int,input().split())
#         for j in range(a-1,b):
#             arr[j].append(i) # 책 번호별 원하는 학생 명단

#     cnt = 0
#     for k in range(len(arr)):
#         if arr[k]:
#             cnt += 1
    
#     print(cnt)

#         # 1-n까지 책중 책을 줄 수 있는 최대 학생 수 

#         # 학생은 a-b 중에 한권 
# import sys
# t=int(input())
# for _ in range(t):
#     n,m=map(int,input().split())

#     visited=[False]*n
#     arr=[[] for _ in range(n)]
#     for i in range(m):
#         a,b=map(int,input().split())

    

# import sys
# input=sys.stdin.readline

# t=int(input())

# for _ in range(t):
#     n,m=map(int,input().split())

#     arr=[list(map(int,input().split())) for _ in range(m)]
#     arr.sort(key=lambda x:x[1]) # 끝나는 시간으로 정렬

#     print(arr)
#     books=[True]*(n+1)

#     answer = 0

#     for s,e in arr:
#         idx=0

#         for i in range(s,e+1):
#             if books[i]:
#                 idx = i
#                 break

#         if idx:
#             books[idx] = False
#             answer += 1

#     print(answer)



import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(m)]

    arr.sort(key=lambda x:x[1]) # 끝나는 번호가 낮은순으로 정렬, 끝나는 수가 작을수록 범위가 작음. 범위가 좁은걸 먼저 해야하니까 

    visited=[True]*(n+1)

    cnt = 0

    for j in arr:
        start = j[0]
        end = j[1]

        for k in range(start,end+1):
            if visited[k] :
                visited[k] = False
                cnt += 1
                break
            


    print(cnt)



        
