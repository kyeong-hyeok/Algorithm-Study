# N개의 자연수 중 M개 N, M = 8
# 같은 수 여러번, 오름차순
# 8^8 = 2^24

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
arr = []


def bt(x):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(x, N):
        arr.append(num[i])
        bt(i)
        arr.pop()


bt(0)