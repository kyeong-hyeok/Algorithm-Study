import sys
import heapq
input=sys.stdin.readline

n = int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:x[1])

room = []
answer = 0 
for i in arr:
    while room and room[0] <= i[1]: # 가장 빨리 끝나는 수업보다 늦게 시작하면 = 겹치지 않음
        heapq.heappop(room)
    heapq.heappush(room,i[2])
    answer = max(answer, len(room))

print(answer)


# n=int(input())
# arr=defaultdict()
# room=[]
# for i in range(n):
#     a,b,c=map(int,input().split())
#     arr[a]=((b,c))

# arr=sorted(arr.items(), key=lambda x : x[1])
# x,y=arr[0][0],arr[0][1]

# for k,(start,end) in arr:

#     for x,y in room:
#         if y <= start :
#             room.remove((x,y))
#             break
#     room.append((start,end))
    
# print(len(room))

        
        
