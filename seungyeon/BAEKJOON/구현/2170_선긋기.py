# 그려진 선들의 총길이
# 최대 최소 

import sys
input=sys.stdin.readline

n = int(input())
arr=list(tuple(map(int,input().split())) for _ in range(n))

arr.sort()
start=arr[0][0]
end=arr[0][1]

answer = 0
for i in range(1,n):
    now_start,now_end=arr[i]

    if end > now_start:
        end = max(end,now_end)
    else:
        answer += (end-start)
        start,end=now_start,now_end

answer += (end-start)
print(answer)
# import sys
# from collections import deque
# input=sys.stdin.readline

# n=int(input())
# answer = 0
# que = deque()
# que.append((1000000000,-1000000000))
# for i in range(n):
#     x,y=map(int,input().split())
#     a,b = que.popleft()
#     if a <= x or y <= b:
#         if x < a :
#             a = x
#         elif b < y :
#             b = y
#         answer = b-a
#         que.append((a,b))
#     else:
#         answer += y-x
#         que.append((x,y))
#     print(que)

# print(answer)