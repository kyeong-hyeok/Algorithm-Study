# N = 100,000

# 생각하지 못한 부분
# 첫번째 전구의 스위치를 누를 때와 누르지 않을 때로 나눠서 생각
# i-1번째의 스위치의 값이 같은지 비교 -> 다르다면 i 스위치 변경

import sys

input_data = sys.stdin.readline

N = int(input_data())
now = list(map(int, input()))
future = list(map(int, input()))


def change(n, f):
    no = n[:]
    cnt = 0
    for i in range(1, N):
        if no[i-1] != f[i-1]:
            cnt += 1
            for j in range(i-1, i+2):
                if j < N:
                    no[j] = 1 - no[j]
    return cnt if no == f else 1e9


r = change(now, future)
now[0] = 1 - now[0]
now[1] = 1 - now[1]
r = min(r, change(now, future)+1)
print(r if r != 1e9 else -1)