# 한 번의 이동에서 합쳐진 블록은 또다른 블록과 합쳐질 수 없음
# 이동하려고 하는 쪽의 칸이 먼저 합쳐짐

# 아이디어
# 회전을 4번 시켜서 위 방향으로만 이동하도록 구현하자! -> 상하좌우 네 방향으로 이동하는 효과
# 이전 이동이 다음 이동에 영향을 줌 -> DFS

# 필요한 메서드
# 1. 회전 -> rotation
# 2. 이동 -> move

# 잘못된 풀이
# 기존 move 메서드 -> 이동 시 빈공간을 올바르게 채우지 못함
# 이동 시, 한 방향에 블록을 모아야 하기 때문에 채워진 마지막 칸을 표시할 "포인터"가 필요함!
# -> pointer를 설정해 블록을 채워가면서 pointer 이동

import sys

input_data = sys.stdin.readline

N = int(input_data())
board = [list(map(int, input_data().split())) for _ in range(N)]


def move(bo):       # 블록 이동 메서드
    for j in range(N):
        pointer = 0     # 포인터 설정
        for i in range(1, N):
            if bo[i][j]:        # 현재 블록이 0이 아닐 때
                tmp = bo[i][j]
                bo[i][j] = 0
                if bo[pointer][j] == 0:     # 포인터에 있는 값이 0이면
                    bo[pointer][j] = tmp
                elif bo[pointer][j] == tmp:     # 포인터에 있는 값이 현재 블록 값이랑 같다면
                    bo[pointer][j] *= 2
                    pointer += 1
                else:       # 포인터에 있는 값이 0이 아니고, 현재 블록 값이랑 다르다면
                    pointer += 1
                    bo[pointer][j] = tmp


def rotation(bo):       # 회전 메서드
    b = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            b[i][j] = bo[N-j-1][i]
    return b


def dfs(index, bo):
    global result
    if index == 5:
        for i in range(N):
            result = max(result, max(bo[i]))
        return
    b = []      # 회전한 보드를 저장하는 리스트
    for _ in range(4):
        b.append(bo)
        bo = rotation(bo)   # 90도 방향 회전
    for o in b:
        move(o)             # 위쪽 방향으로 블록 이동
        dfs(index + 1, o)


result = 0
dfs(0, board)
print(result)