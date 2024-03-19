# 가로선이 연속하거나 접하면 안 됨
# N = 10, H = 30, M = 300
# 백트래킹

# 디버깅
# check 함수에서 line[i][x]를 line[i][j]로 함 . .

import sys

input_data = sys.stdin.readline

N, M, H = map(int, input_data().split())
line = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input_data().split())
    line[a][b] = 1


def check():      # O(N) * O(H) = O(300)
    for j in range(1, N+1):
        x = j
        for i in range(1, H+1):
            if line[i][x]:
                x += 1
            elif line[i][x-1]:
                x -= 1
        if x != j:
            return 0
    return 1


def bt(h, k):
    global result
    if k > 3:
        return
    if check():
        result = min(result, k)
        return
    for i in range(h, H+1):
        for j in range(1, N):
            if not (line[i][j] or line[i][j-1] or line[i][j+1]):
                line[i][j] = 1
                bt(i, k+1)
                line[i][j] = 0


result = 5
bt(1, 0)
if result > 3:
    print(-1)
else:
    print(result)


# 이전 풀이
# 딕셔너리를 이용한 가로선 체크 -> 시간 초과
# 디버깅
# 처음에 입력받을 때 line_dict[(a-1, b-1)] = 1 을 line_dict[(a, b)] = 1 로 함

import sys

input_data = sys.stdin.readline

N, M, H = map(int, input_data().split())
line = []
line_dict = dict()
for _ in range(M):
    a, b = map(int, input_data().split())
    line.append((a-1, b-1))
    line_dict[(a-1, b-1)] = 1


def go_down():      # O(N) * O(H) = O(300)
    for j in range(N):
        x = j
        for i in range(H):
            if (i, x) in line_dict:
                x += 1
            elif (i, x-1) in line_dict:
                x -= 1
        if x != j:
            return 0
    return 1


def bt(h, k):
    global result
    if k > 3:
        return
    if go_down():
        result = min(result, k)
        return
    for j in range(h, H):
        for i in range(N):
            if (j, i) not in line_dict and (j, i-1) not in line_dict and (j, i+1) not in line_dict:
                line.append((j, i))
                line_dict[(j, i)] = 1
                bt(j, k+1)
                del line_dict[(j, i)]
                line.pop()


result = 5
bt(0, 0)
if result == 5:
    print(-1)
else:
    print(result)