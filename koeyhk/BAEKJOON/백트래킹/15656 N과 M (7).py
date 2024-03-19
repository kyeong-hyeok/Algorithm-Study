# N, M = 7
# N개의 자연수 중 M개 - 중복 가능
# 백트래킹

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
numbers = list(map(int, input_data().split()))
numbers.sort()
arr = []


def bt():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(N):
        arr.append(numbers[i])
        bt()
        arr.pop()

bt()