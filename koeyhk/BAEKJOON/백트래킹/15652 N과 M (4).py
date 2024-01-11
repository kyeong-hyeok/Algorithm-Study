# 길이가 M인 수열 모두 구하기 - 같은 수 여러 번 가능, 오름차순

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
arr = []


def bt(x):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(x, N):
        arr.append(i+1)
        bt(i)
        arr.pop()


bt(0)