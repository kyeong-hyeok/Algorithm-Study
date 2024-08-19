# 문제 요약
# NxM, CCTV 회전은 90도 방향
# 1~5: CCTV 번호, 6: 벽
# CCTV는 CCTV 통과 가능
# 사각지대의 최소 크기? -> CCTV의 방향이 중요
# 완전탐색 가능

# 잘못 생각한 풀이
# 1. cctv 순서대로 사각지대 적어지는 방향으로 설정함
# -> 이전에 결정된 cctv 방향이 다음 cctv 방향에 영향을 줌 - 전체로 봤을 때 최솟값이 아닐 수 있음!

# 개선이 필요한 코드
# 1. cctv 번호에 따라 회전하는 과정을 거치지 않고, 해당 방향들을 모두 2차원 리스트에 저장하는 것이 효율적임 (각 cctv 최대 4개의 방향)
# dir = [[], [0], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]]

# 정답 풀이
# 1. cctv 마다 모든 경우의 수를 고려해야 함 -> 최대 경우의 수 4^8
# 이전 cctv 방향 선택이 다음 cctv 방향 선택에 영향을 줌 -> DFS로 접근
# 모든 cctv의 방향 설정이 완료됐을 경우 최솟값 갱신

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
office = []
for i in range(N):
    office.append(list(map(int, input_data().split())))

cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j, office[i][j]))

# 번호별 cctv 방향 설정
dir = [[[]],
       [[0], [1], [2], [3]],
       [[1, 3], [0, 2]],
       [[0, 1], [1, 2], [2, 3], [0, 3]],
       [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
       [[0, 1, 2, 3]]]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(index, of):
    global result
    if index == len(cctv):  # 모든 cctv의 방향 설정 완료 시
        cnt = 0
        for i in range(N):
            cnt += of[i].count(0)
        result = min(result, cnt)
        return
    x, y, num = cctv[index][0], cctv[index][1], cctv[index][2]
    for di in dir[num]:
        tmp = [o[:] for o in of]    # 배열 복사
        for d in di:        # cctv 방향에 따라 감시할 수 있는 영역 설정
            nx, ny = x + dx[d], y + dy[d]
            while 1:
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break
                if tmp[nx][ny] != 6:
                    if tmp[nx][ny] == 0:
                        tmp[nx][ny] = 7
                else:
                    break
                nx, ny = nx + dx[d], ny + dy[d]
        dfs(index+1, tmp)       # 다음 cctv로 dfs 수행


result = 100
dfs(0, office)
print(result)
