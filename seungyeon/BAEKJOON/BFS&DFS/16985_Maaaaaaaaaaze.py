# 가장 적은 이동 횟수로 출구에 도달하기에 bfs 사용해야겠다고 생각!
# 현재 칸에서 이동할 수 없을 때 판 회전하기, 인접한 칸 찾아서 큐에 넣기  라고 생각했는데 
# 문제를 제대로 읽어야함. 참가자 마음대로 판 순서 배치 가능
# 따라서 판 순서 배치해두고, 배치해둔 것의 최솟값을 구해야함

import sys
from collections import deque
from itertools import permutations
input=sys.stdin.readline

arr=[[list(map(int,input().split())) for _ in range(5)] for _ in range(5)]
board=[[[0]* 5 for _ in range(5)] for _ in range(5)]
result = sys.maxsize

dh = (0,0,0,0,1,-1)
dy = (0,0,1,-1,0,0)
dx=(1,-1,0,0,0,0)

# 참가자 마음대로 판 쌓기 -> 5개 중 5개 원하는 순서대로 나열하는 경우 
def solve():
    for d in permutations([0,1,2,3,4]):
        for i in range(5):
            board[d[i]] = arr[i]
        dfs(0)

def rotate(b):
    tmp = [[0]* 5 for _ in range(5)]

    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4-i] = b[i][j] # 90도 회전
    
    return tmp

# 배열을 90도씩 돌리며 재귀함수 요청. 다 돌리고 bfs로 최소거리 찾기 
def dfs(d): 
    global board

    if d == 5:
        if board[4][4][4]:
            bfs(board)
        return
    
    for i in range(4):
        if board[0][0][0]:
            dfs(d+1)
        board[d] = rotate(board[d])

def bfs(b):
    global result
    que = deque()
    dist=[[[0,0,0,0,0] for _ in range(5)] for _ in range(5)]
    que.append((0,0,0))

    while que:
        h,y,x = que.popleft()

        if (h,x,y) == (4,4,4):
            result = min(result,dist[4][4][4])
            if result == 12:
                print(result)
                exit()
            return 
        
        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]


            if nh < 0 or nh >= 5 or ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue
            elif b[nh][ny][nx] == 0 or dist[nh][ny][nx] != 0:
                continue
            que.append((nh,ny,nx))
            dist[nh][ny][nx] = dist[h][y][x] + 1

solve()
if result == sys.maxsize:
    result = -1
print(result)