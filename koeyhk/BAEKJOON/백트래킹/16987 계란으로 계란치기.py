# 계란의 내구도 -= 상대 무게
# 계란의 내구도 <= 0 -> 깨짐
# 최대 몇 개의 계란?
# 8^8 = 2^24 = 16 * 1000 * 1000
# 백트래킹 + 구현

import sys

input_data = sys.stdin.readline

N = int(input_data())
eggs = [list(map(int, input_data().split())) for _ in range(N)]
result = 0


def break_egg(x):
    global result
    if x == N:      # 문제 조건 3번 - 종료
        r = 0
        for i in range(N):
            if eggs[i][0] <= 0:
                r += 1
        result = max(result, r)
    elif eggs[x][0] <= 0:       # 문제 조건 2번 - 손에 든 계란 깨진 경우
        break_egg(x+1)
    else:
        b = 0
        for i in range(N):      # 문제 조건 2번 - 손에 든 계란으로 다른 계란 치기
            if i == x:
                continue
            if eggs[i][0] > 0:
                b = 1
                eggs[x][0] -= eggs[i][1]
                eggs[i][0] -= eggs[x][1]
                break_egg(x+1)
                eggs[x][0] += eggs[i][1]
                eggs[i][0] += eggs[x][1]
        if b == 0:          # 문제 조건 2번 - 깨지지 않은 계란이 없을 경우
            break_egg(N)


break_egg(0)
print(result)