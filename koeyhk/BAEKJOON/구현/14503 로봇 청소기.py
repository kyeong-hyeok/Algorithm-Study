# N, M = 50
# d 북 동 남 서
# 지역의 값 0 -> 청소 x, 1 -> 벽
# 청소 x -> 청소
# 1. 주변 4칸 중 청소되지 않은 칸이 없는 경우
# -> 방향유지, 후진할 수 있다면 후진
# -> 후진 불가능하다면 멈춤
# 2. 주변 4칸 중 청소되지 않은 칸이 있는 경우
# 반시계 방향 회전 -> 앞쪽 칸이 청소되지 않은 빈 칸인 경우 전진 -> 반복

# 문제 접근
# 문제에서 주어진 작동 방식이 있다면 빠지지 않고 조건을 충족시키면 정답!

# 놓친 조건
# 후진 시 벽이 아닌지 확인!

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
r, c, d = map(int, input_data().split())
room = [list(map(int, input_data().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0


def check(x, y):    # 주변 4칸 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            return 1
    return 0


def move(x, y, d):
    global result
    if room[x][y] == 0:
        result += 1
        room[x][y] = -1
    if check(x, y):
        for i in range(4):
            d = (d+3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                break
        move(nx, ny, d)
    else:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] != 1:
            move(nx, ny, d)
        else:
            return


move(r, c, d)
print(result)