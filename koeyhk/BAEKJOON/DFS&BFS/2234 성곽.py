# 방의 개수, 가장 넓은 방 넓이, 하나의 벽을 제거해 얻을 수 있는 가장 넓은 방 크기
# M, N = 50
# 방의 개수 DFS -> 가장 넓은 방 넓이

# 풀이 아이디어
# move 리스트를 만들어 [북, 동, 남, 서]로 움직일 수 있는 여부 체크해 저장
# dfs의 조건에 move 추가
# 하나의 벽을 제거하는 것 -> 새로운 dfs로 벽을 한 번만 이동할 수 있도록 변수 설정

import sys
sys.setrecursionlimit(10**9)
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
castle = [list(map(int, input_data().split())) for _ in range(M)]
move = [[[1, 1, 1, 1] for _ in range(N)] for _ in range(M)]

for i in range(M):
    for j in range(N):
        tmp = castle[i][j]
        if tmp >= 8:
            tmp -= 8
            move[i][j][2] = 0
        if tmp >= 4:
            tmp -= 4
            move[i][j][1] = 0
        if tmp >= 2:
            tmp -= 2
            move[i][j][0] = 0
        if tmp >= 1:
            tmp -= 1
            move[i][j][3] = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0]*N for _ in range(M)]


def dfs(x, y):
    global k
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and move[x][y][i] == 1 and visited[nx][ny] == 0:
            k += 1
            visited[nx][ny] = 1
            dfs(nx, ny)


cnt, result = 0, 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            k = 1
            cnt += 1
            visited[i][j] = 1
            dfs(i, j)
            result = max(result, k)


def dfs(x, y):
    global k, c
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0:
            if move[x][y][i] == 1:
                k += 1
                visited[nx][ny] = 1
                dfs(nx, ny)
            elif c < 1:
                k += 1
                c += 1
                visited[nx][ny] = 1
                dfs(nx, ny)


answer = 0
for i in range(M):
    for j in range(N):
        visited = [[0]*N for _ in range(M)]
        k = 1
        visited[i][j] = 1
        c = 0
        dfs(i, j)
        answer = max(answer, k)

print(cnt)
print(result)
print(answer)