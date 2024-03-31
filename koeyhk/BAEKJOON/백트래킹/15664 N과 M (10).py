# N개 자연수, 길이 M인 수열
# 중복되는 수열 x, 각 수열은 공백으로 구분 출력, 오름차순
# 백트래킹

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
arr = []
d = dict()


def bt(x):
    if len(arr) == M:
        if ''.join(map(str, arr)) not in d:
            print(*arr)
            d[''.join(map(str, arr))] = 1
            return
    for i in range(x, N):
        arr.append(num[i])
        bt(i+1)
        arr.pop()


bt(0)