import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
office = [list(map(int, input_data().split())) for _ in range(N)]

c = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            c.append((i, j))

cctv = [[],         # cctv 번호에 따른 모든 감시 방향!
        [[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [0, 3]],
        [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
        [[0, 1, 2, 3]]]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(index, of):
    global result
    if index == len(c):     # 모든 cctv 감시 영역 확인했을 경우
        count = 0
        for i in range(N):
            count += of[i].count(0)
        result = min(result, count)
        return
    x, y = c[index][0], c[index][1]
    for directions in cctv[office[x][y]]:   # 해당 cctv 번호에 따른 감시 방향
        a = [arr[:] for arr in of]      # 배열 복사
        for d in directions:            # 각 방향에 따른 for 문
            nx, ny = x, y
            while 1:
                nx += dx[d]
                ny += dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                elif a[nx][ny] == 6:
                    break
                elif a[nx][ny] == 0:
                    a[nx][ny] = 7
        dfs(index+1, a)         # 다음 cctv에 대한 dfs 수행


result = int(1e9)
dfs(0, office)
print(result)