# 5! * 4^5 * 25 * 5 = 120 * 1024 * 125 -> BFS + 완전 탐색
# 구현 문제는 디버깅이 중요하다 !!! 

# 놓친 부분
# 모서리 끝 부분 칸을 확인할 때 b[0][0] == 1 로 확인함 (x) -> b[0][0][0] == 1로 해야 함

import sys
from collections import deque
from itertools import permutations

input_data = sys.stdin.readline
board = [[list(map(int, input_data().split())) for _ in range(5)] for _ in range(5)]
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def rotation(b):
    tmp = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            tmp[j][i] = b[4-i][j]
    return tmp


def bfs(bo):
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5 and bo[nx][ny][nz] == 1 and visited[nx][ny][nz] == 0:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))
                if nx == 4 and ny == 4 and nz == 4:
                    return visited[nx][ny][nz] - 1
    return -1


result = 100000

for i in list(permutations([0, 1, 2, 3, 4], 5)):
    b = [board[i[0]], board[i[1]], board[i[2]], board[i[3]], board[i[4]]]
    for _ in range(4):
        b[0] = rotation(b[0])
        if b[0][0][0] == 0:
            continue
        for _ in range(4):
            b[4] = rotation(b[4])
            if b[4][4][4] == 0:
                continue
            for _ in range(4):
                b[1] = rotation(b[1])
                for _ in range(4):
                    b[2] = rotation(b[2])
                    for _ in range(4):
                        b[3] = rotation(b[3])
                        k = bfs(b)
                        if k != -1:
                            result = min(result, k)

if result == 100000:
    print(-1)
else:
    print(result)