# 경사로 높이 1, 길이 L -> 낮은 칸에 놓음 L개의 연속된 칸 모두 같은 높이
# 경사로 놓은 곳에 또 놓을 수 없음
# N, L = 100

# 문제 풀면서 생각한 것
# 해당 행 또는 열을 reverse 해야할까? -> X 앞 뒤를 비교해서 경사로를 세우면 됨
# 경사로를 세운 후 visited 갱신

# 문제 조건을 빠뜨리지 않고 구현하는 것이 중요하다!
# 적당한 틀을 잡아두고 구현하면서 조건 추가하기

import sys

input_data = sys.stdin.readline

N, L = map(int, input_data().split())
board = [list(map(int, input_data().split())) for _ in range(N)]


def check(bo):
    b = bo[:]
    i = len(b) - 2
    visited = [0] * len(b)
    while i >= 0:
        if b[i] == b[i + 1]:    # 높이가 같다면 continue
            i -= 1
            continue
        if abs(b[i] - b[i + 1]) != 1:   # 높이가 1 차이가 아니라면 0 return
            return 0
        if b[i] < b[i+1]:       # 높이: i < i + 1
            if i - L + 1 < 0:
                return 0
            for j in range(i, i - L, -1):
                if b[j] != b[i] or visited[j] == 1:
                    return 0
                visited[j] = 1
            if i-L >= 0 and b[i-L] > b[i-L+1]:
                return 0
            i -= L
        else:                   # 높이: i > i + 1
            if i + L > len(b) - 1:
                return 0
            for j in range(i+1, i + L + 1):
                if b[j] != b[i+1] or visited[j] == 1:
                    return 0
                visited[j] = 1
            if i+L+1 < len(b) and b[i+L+1] > b[i+L]:
                return 0
            i -= 1
    return 1


result = 0
for i in range(N):
    result += check(board[i])
for i in range(N):
    bo = []
    for j in range(N):
        bo.append(board[j][i])
    result += check(bo)
print(result)