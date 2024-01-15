# 불을 퍼트리고 사람이 이동해야한다.
# 사람이 격자 밖으로 나갈 수 있는지 확인해야한다
# 불이 퍼진 정보를 저장하고 이를 기반으로 bfs로 이동
# 최단 거리 = bfs


import sys
input=sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


# 불이 퍼지는 과정
def fire_bfs():
    while fire_queue:
        r,c = fire_queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if arr[nr][nc] == "#" or fire[nr][nc]:
                continue
            fire[nr][nc] = fire[r][c] + 1
            fire_queue.append((nr,nc))

def human_bfs():
    while human_queue:
        r,c = human_queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < R and 0 <= nc < C):
                print(human[r][c])
                return
            if human[nr][nc] or arr[nr][nc] == "#":
                continue
            if fire[nr][nc] and human[r][c] + 1 >= fire[nr][nc]:
                continue
            human[nr][nc] = human[r][c] + 1
            human_queue.append((nr,nc))
    print("IMPOSSIBLE")
    return 

R,C = map(int,input().split())
arr = []
fire_queue = deque()
human_queue = deque()

human = [[0]*C for _ in range(R)]
fire = [[0]*C for _ in range(R)]
for i in range(R):
    arr.append(list(input().strip()))
    for j in range(C):
        if arr[i][j] == "J":
            human_queue.append((i,j))
            human[i][j] = 1
        elif arr[i][j] == "F":
            fire_queue.append((i,j))
            fire[i][j] = 1

fire_bfs()
human_bfs()
