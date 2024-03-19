# 7명, 자리 인접, 반드시 이다솜파만 x, 이다솜파가 우위(7명 중 4명 이상)
# DFS -> 탐색해서 7명 찾기
# 중복 제거 -> visited 1인거 순서대로 인덱스 str로 만들어 딕셔너리 저장
# 백트래킹(DFS)

# 처음에 생각하지 못 한 부분
# 기존 DFS로만 문제를 푼다면 최근에 입력된 좌표에서 깊이 들어가기만 해서 모든 경우의 수 찾지 못 함
# **방문한 지역들 각각에서 DFS 수행**


import sys

input_data = sys.stdin.readline
cla = [list(input_data().rstrip()) for _ in range(5)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
arr = []


def bt(x, y, cnt):
    global result
    if len(arr) == 7:
        if cnt >= 4:
            s = ''.join(map(str, sorted(arr)))
            if s not in d:
                d[s] = 1
                result += 1
        return
    for a in arr:       # O((4^7) * 7*8/2) = O(1000*16*28)
        x, y = a[0], a[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                arr.append((nx, ny))
                if cla[nx][ny] == 'S':
                    bt(nx, ny, cnt + 1)
                else:
                    bt(nx, ny,  cnt)
                arr.pop()
                visited[nx][ny] = 0


result = 0
d = dict()
visited = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        visited[i][j] = 1
        arr.append((i, j))
        if cla[i][j] == 'S':
            bt(i, j, 1)
        arr.pop()
        visited[i][j] = 0
print(result)