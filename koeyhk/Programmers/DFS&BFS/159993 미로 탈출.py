# 레버를 당기고, 출구로 가야 하기 때문에
# (시작 지점 ~ 레버 최단 시간 + 레버 ~ 출구 최단 시간)을 구하면 된다.

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(lm, x, y, type):    # type은 L(레버), E(출구)
    visited = [[0]*len(lm[0]) for _ in range(len(lm))]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(lm) and 0 <= ny < len(lm[0]) and visited[nx][ny] == 0:
                if lm[nx][ny] != 'X':   # 벽이 아니라면
                    q.append((nx, ny))      # 방문할 곳으로 추가
                    visited[nx][ny] = visited[x][y] + 1
                    if lm[nx][ny] == type:  # type에 도착했다면 반환
                        return visited[nx][ny] - 1
    return -1


def solution(maps):
    lm = []
    for m in maps:
        lm.append(list(m))
    for i in range(len(lm)):
        for j in range(len(lm[0])):
            if lm[i][j] == 'S':     # 시작 지점
                x, y = i, j
            elif lm[i][j] == 'L':   # 레버 지점
                rx, ry = i, j
    l = bfs(lm, x, y, 'L')      # 시작 지점 ~ 레버 최단 시간
    e = -1
    if l != -1:
        e = bfs(lm, rx, ry, 'E')    # 레버 ~ 출구 최단 시간
        if e != -1:
            e += l
        else:
            e = -1
    return e