# N = 20

# 문제 접근
# 번호대로 좋아하는 학생이 앉아 있다면
# -> 해당 학생이 앉은 번호 주변 count += 1
# -> max_count 저장
# board를 돌면서 max_count와 같고 인접한 빈 자리가 가장 많은 좌석 선택
# 인접한 자리 개수 갱신

# 다른 풀이 방법
# board를 돌면서 해당 좌석이 빈 좌석일 경우
# -> 해당 좌석이 인접한 칸에 좋아하는 학생이 있다면 like += 1
# -> 해당 좌석이 인접한 칸이 비어있다면 empty += 1
# result에 like, empty, x, y 각각 저장
# 마지막에 sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))

import sys

input_data = sys.stdin.readline

N = int(input_data())
seat = [list(map(int, input_data().split())) for _ in range(N*N)]
board = [[0]*N for _ in range(N)]
now_seat = [[-1, -1] for _ in range(N*N + 1)]   # 번호별 앉아 있는 자리
empty = [[4]*N for _ in range(N)]               # 비어있는 칸의 수 각각 저장
for i in range(1, N-1):
    empty[0][i], empty[N-1][i], empty[i][0], empty[i][N-1] = 3, 3, 3, 3
empty[0][0], empty[0][N-1], empty[N-1][N-1], empty[N-1][0] = 2, 2, 2, 2

seated = dict()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(len(seat)):
    stu = seat[i][0]
    se = seat[i][1:]
    max_count = 0
    count = [[0] * N for _ in range(N)]
    for s in se:
        if s in seated:
            x, y = now_seat[s][0], now_seat[s][1]
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                    count[nx][ny] += 1
                    max_count = max(max_count, count[nx][ny])     # 좋아하는 학생이 인접한 칸의 최대 수 구하기
    e_m = -1    # 인접한 칸 중에서 비어있는 칸의 개수
    nx, ny = -1, -1
    for x in range(N):
        for y in range(N):
            if count[x][y] == max_count and board[x][y] == 0:     # 좋아하는 학생이 가장 많고,
                if e_m < empty[x][y]:                       # 인접한 칸 중 비어있는 칸이 가장 많은 곳일 때
                    e_m = empty[x][y]
                    nx, ny = x, y
    board[nx][ny] = stu
    seated[stu] = 1     # 해당 번호 좌석에 앉았다는 표시
    now_seat[stu] = [nx, ny]    # 현재 앉은 사람의 자리 갱신
    for j in range(4):
        kx, ky = nx + dx[j], ny + dy[j]
        if 0 <= kx < N and 0 <= ky < N:
            empty[kx][ky] -= 1

seat.sort()
result = 0
for i in range(1, len(now_seat)):       # 번호 순서대로 만족도 구하기
    x, y = now_seat[i][0], now_seat[i][1]
    cnt = 0
    for j in range(4):
        nx, ny = x + dx[j], y + dy[j]
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] in seat[i-1]:
                cnt += 1
    if cnt > 0:
        result += pow(10, cnt-1)

print(result)