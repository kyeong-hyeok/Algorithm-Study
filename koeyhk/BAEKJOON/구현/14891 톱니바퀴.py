# 풀이 1
# 회전 전에 맞닿은 톱니의 극이 다르면 반대 방향으로 회전
# 0번 - 2 1번 - 6, 1번 - 2 2번 - 6, 2번 - 2 3번 - 6
# 회전 계획을 세워두고 마지막에 회전? ㅇㅋ
# 0->1->2->3
# 1->0->2->3
# 2->3->1->0
# 3->2->1->0

# 틀렸던 부분
# 1. 두 극이 같다면 같은 방향으로 회전하는 것이 아니라 회전하지 않음!

import sys

input_data = sys.stdin.readline

top = [list(map(int, input_data().rstrip())) for _ in range(4)]
K = int(input_data())
rotation = [list(map(int, input_data().split())) for _ in range(K)]


def rot(num, prevnum, r):
    if prevnum < num:
        if top[prevnum][2] != top[num][6]:
            return -r
        else:
            return 0
    else:
        if top[prevnum][6] != top[num][2]:
            return -r
        else:
            return 0

# 0->1 1->2 ... 6->7 7->0
# 1->0 2->1 ... 7->6


def move(x, r):
    if r == 1:
        tmp = x[7]
        for i in range(7, 0, -1):
            x[i] = x[i-1]
        x[0] = tmp
    elif r == -1:
        tmp = x[0]
        for i in range(7):
            x[i] = x[i+1]
        x[7] = tmp


for ro in rotation:
    num = ro[0]-1
    r = ro[1]
    if num == 0:
        a = r
        b = rot(1, 0, r)
        c = rot(2, 1, b)
        d = rot(3, 2, c)
    elif num == 1:
        b = r
        a = rot(0, 1, r)
        c = rot(2, 1, r)
        d = rot(3, 2, c)
    elif num == 2:
        c = r
        b = rot(1, 2, r)
        a = rot(0, 1, b)
        d = rot(3, 2, r)
    else:
        d = r
        c = rot(2, 3, r)
        b = rot(1, 2, c)
        a = rot(0, 1, b)
    move(top[0], a)
    move(top[1], b)
    move(top[2], c)
    move(top[3], d)


result = 0
for i in range(4):
    result += top[i][0] * pow(2, i)

print(result)


# 풀이 2
# 1. collections의 deque -> rotate() 라이브러리
# rotate(1) - 리스트가 오른쪽으로 이동
# rotate(-1) - 리스트가 왼쪽으로 이동

# 2. 각각 하나씩 직접 rotate 여부를 확인하지 않고 왼쪽 오른쪽으로 나눠서 재귀!
# 회전하는 경우 -> 다음 톱니바퀴 확인
# 회전하지 않는 경우 -> 확인 x

import sys
from collections import deque

input_data = sys.stdin.readline

top = list(deque(map(int, input_data().rstrip())) for _ in range(4))
K = int(input_data())
rotation = [list(map(int, input_data().split())) for _ in range(K)]


def right(num, r):
    if num < 4:
        if top[num-1][2] != top[num][6]:
            right(num+1, -r)
            top[num].rotate(r)
    return


def left(num, r):
    if num >= 0:
        if top[num+1][6] != top[num][2]:
            left(num-1, -r)
            top[num].rotate(r)
    return


for ro in rotation:
    x = ro[0] - 1
    r = ro[1]
    left(x-1, -r)
    right(x+1, -r)
    top[x].rotate(r)

result = 0
for i in range(4):
    result += top[i][0] * pow(2, i)

print(result)





