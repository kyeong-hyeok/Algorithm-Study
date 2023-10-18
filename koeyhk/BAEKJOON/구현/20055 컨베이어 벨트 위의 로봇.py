# N <= 100, Ai <= 1000
# 단계별로 진행하는 데 있어서 시간 초과는 나지 않을 것이라 생각!

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
A = list(map(int, input_data().split()))
loc = [i for i in range(2*N)]
robot = [0 for i in range(2*N)]
count = 0

while 1:
    temp = loc[2*N-1]
    for i in range(2*N-2, -1, -1):
        loc[i+1] = loc[i]
    robot[loc[N-1]] = 0
    loc[0] = temp
    for i in range(N-2, -1, -1):
        if robot[loc[i]] == 1:
            if A[loc[i+1]] >= 1 and robot[loc[i+1]] == 0:
                A[loc[i+1]] -= 1
                robot[loc[i]] = 0
                robot[loc[i+1]] = 1
    robot[loc[N - 1]] = 0
    if A[loc[0]] > 0:
        robot[loc[0]] = 1
        A[loc[0]] -= 1
    s = 0
    for i in A:
        if i <= 0:
            s += 1
    count += 1
    if s >= K:
        print(count)
        break
