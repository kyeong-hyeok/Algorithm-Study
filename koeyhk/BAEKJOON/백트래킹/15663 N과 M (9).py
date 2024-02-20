# 수정한 풀이

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
visited = [0] * N
arr = []
result = set()


def bt():
    if len(arr) == M:
        if tuple(arr) not in result:
            result.add(tuple(arr))
            print(*arr)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num[i])
            bt()
            visited[i] = 0
            arr.pop()


bt()


# 이거 왜 안 될까 . .
# -> 11 1, 1 11 일 경우 다르지만 합쳐져서 111 111 로 중복 처리가 됨!!!!

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
num = list(map(int, input_data().split()))
num.sort()
d = dict()
visited = [0] * N
arr = []

def bt():
    if len(arr) == M:
        if ''.join(map(str, arr)) not in d:
            d[''.join(map(str, arr))] = 1
            print(*arr)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num[i])
            bt()
            visited[i] = 0
            arr.pop()


bt()