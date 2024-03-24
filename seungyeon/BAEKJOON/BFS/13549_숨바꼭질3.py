import sys
from collections import deque

input=sys.stdin.readline

n,k = map(int,input().split())

que = deque()
que.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0


while que:
    s = que.popleft() # 방문할 노드

    if s == k:
        print(visited[s])
        break

    if 0 <= s-1 < 100001 and visited[s-1] == -1: # x-1 하는 경우, x-1 이 방문한 적 없는 경우
        visited[s-1] = visited[s] + 1
        que.append(s-1)
    if 0 < s*2 < 100001 and visited[s*2] == -1: # x*2 하는 경우, x*2가 방문한 적 없는 경우
        visited[s*2] = visited[s]
        que.appendleft(s*2)
    if 0 <= s+1 < 100001 and visited[s+1] == -1: # x+1 하는 경우, x+1 이 방문한 적 없는 경우
        visited[s+1] = visited[s] + 1
        que.append(s+1)