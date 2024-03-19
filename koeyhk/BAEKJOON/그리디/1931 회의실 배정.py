# 가능한 회의 중 가장 먼저 끝나는 회의를 택하기 !
# 현재 시간이 t라고 할 때 시작 시간이 t 이상인 모든 회의 중에서 가장 먼저 끝나는 회의를 택하는 것이 최적해
# 끝나는 시간이 빠른 순, 시작 시간이 빠른 순 ex) 2 2, 1 2 고려

import sys

input_data = sys.stdin.readline

N = int(input_data())
meet = []
for i in range(N):
    s, e = map(int, input_data().split())
    meet.append((s, e))
meet.sort(key=lambda x: (x[1], x[0]))
cnt = 1
k = 0
for i in range(1, len(meet)):
    d = 0
    if meet[k][1] <= meet[i][0]:
        k = i
        cnt += 1

print(cnt)