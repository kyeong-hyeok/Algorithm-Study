# 최소 한 개의 모음 (5개), 최소 두 개의 자음 (21개), 오름차순 배열
# 문자의 종류 C가지
# 백트래킹

# 놓쳤던 부분
# 최소 한 개의 모음, 최소 두 개의 자음 -> 모음만 신경쓰면 안 됨, 두 조건 모두 충족

import sys

input_data = sys.stdin.readline

L, C = map(int, input_data().split())
str = list(input_data().split())
str.sort()
arr = []
visited = [0] * C


def bt(x):
    if len(arr) == L:
        a = 0
        b = 0
        for i in arr:
            if i in ('a', 'e', 'i', 'o', 'u'):
                a = 1
            else:
                b += 1
        if a == 1 and b >= 2:
            print(''.join(arr))
        return
    for i in range(x, C):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(str[i])
            bt(i+1)
            arr.pop()
            visited[i] = 0


bt(0)