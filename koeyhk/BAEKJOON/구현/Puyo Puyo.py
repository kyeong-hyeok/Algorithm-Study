# 동시에 터져야 함 -> 여러 그룹이 터져도 한 번의 연쇄만 추가

# 필요한 함수
# 1. 터질 뿌요가 있는지 확인하는 함수 - BFS
# 2. 뿌요를 터뜨리는 함수
# 3. 뿌요를 아래로 이동시키는 함수

import sys
from collections import deque

input_data = sys.stdin.readline

arr = [list(input_data().rstrip()) for _ in range(12)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bomb():
    bb = 0
    for i in range(11):
        for j in range(6):
            if arr[i][j] == 'R' or arr[i][j] == 'G' or arr[i][j] == 'B' or arr[i][j] == 'P' or arr[i][j] == 'Y':
                bo = [(i, j)]
                result = bfs(i, j, arr[i][j], bo)
                if result >= 4:
                    for b in bo:
                        arr[b[0]][b[1]] = '.'
                    bb = 1
    return bb


def bfs(x, y, color, bomb_list):
    result = 1
    q = deque()
    q.append((x, y))
    visited = [[0] * 6 for _ in range(12)]
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == color and visited[nx][ny] == 0:
                result += 1
                visited[nx][ny] = 1
                bomb_list.append((nx, ny))
                q.append((nx, ny))
    return result


def move():
    for i in range(6):
        pointer = 0
        for j in range(11, -1, -1):
            if arr[j][i] == '.' and j > pointer:
                pointer = j
            elif arr[j][i] != '.' and pointer > j:
                arr[pointer][i] = arr[j][i]
                arr[j][i] = '.'
                pointer -= 1


answer = 0
while 1:
    if bomb() == 0:
        print(answer)
        break
    else:
        answer += 1
        move()