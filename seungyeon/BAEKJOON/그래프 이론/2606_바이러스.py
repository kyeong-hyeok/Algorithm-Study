import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
m=int(input())

arr=[ [ ]for i in range(n+1)] # 리스트 컴프리헨션
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(k):

    answer = 0
    que = deque()

    que.append(k)

    while que:
        a = que.popleft()
        visited[a] = True # 이거 안써서 틀렸었음

        for i in arr[a]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                answer += 1

    return answer

print(bfs(1))

