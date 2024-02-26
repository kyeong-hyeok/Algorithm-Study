# R, C = 20
# BFS + Set -> Python3 통과

# 생각하지 못 했던 부분
# 1. deque -> Set으로 변경해 중복된 값에 대한 연산을 줄임
# 2. 이전에 방문했던 값들과 현재 방문하는 값들을 더해 문자열을 만들어 중복 확인

import sys
input_data = sys.stdin.readline

R, C = map(int, input_data().split())
board = [list(input_data().rstrip()) for _ in range(R)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
result = 0


def bfs(x, y):
    global result
    q = set()
    q.add((x, y, board[x][y]))
    while q:
        x, y, s = q.pop()
        result = max(result, len(s))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in s:
                q.add((nx, ny, s + board[nx][ny]))


bfs(0, 0)
print(result)


# 백트래킹 + DFS
# PyPy3로 통과

# 생각하지 못 한 부분
# ord()함수 - 아스키 코드로 변환하는 함수

import sys

input_data = sys.stdin.readline

R, C = map(int, input_data().split())
board = [list(input_data().rstrip()) for _ in range(R)]
b = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        b[i][j] = ord(board[i][j])
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
visited = [0] * 100
result = 0


def dfs(x, y, k):
    global result
    result = max(result, k)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and visited[b[nx][ny]] == 0:
            visited[b[nx][ny]] = 1
            dfs(nx, ny, k+1)
            visited[b[nx][ny]] = 0


visited[b[0][0]] = 1
dfs(0, 0, 1)
print(result)