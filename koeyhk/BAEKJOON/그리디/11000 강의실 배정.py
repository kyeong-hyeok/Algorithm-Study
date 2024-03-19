# 문제 풀 때 생각한 부분
# N = 200,000 -> O(N^2) 이하
# 일찍 시작하는 강의부터 강의실 배정 -> 끝나는 시간 해시로 저장?
# 끝나는 시간보다 현재 선택한 강의의 시작 시간이 이전이면 강의실 늘려야함
# 현재 이용 가능한 강의실 수, 전체 강의실 수, 이전 시간?

# 잘못 생각한 부분
# 회의의 시작, 종료 시간을 함께 고려하려고 함 -> 정렬 조건 2개
# (종료 -> 시작 시간)으로 정렬하면 현재 회의의 시작 시간과 가장 빠른 종료 시간을 비교할 때 최적의 해를 보장하지 않음
# 정정: 현재 확인할 회의는 시작 시간 순으로 정렬되어 있어야 하고, 비교할 회의는 가장 빠른 종료 시간을 가지고 있는 회의여야 함

# 놓친 부분
# 우선순위 큐 사용 -> 종료 시간이 빠른 회의실부터 현재 회의와 비교 해야함!
# 따라서 time 리스트는 시작 시간 순으로 정렬하고 우선 순위 큐를 만들어 종료 시간 넣기

import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data())
time = [list(map(int, input_data().split())) for _ in range(N)]
time.sort()

cnt = 1
q = []
heapq.heappush(q, time[0][1])

for i in range(1, N):
    if time[i][0] < q[0]:
        cnt += 1
    else:
        heapq.heappop(q)
    heapq.heappush(q, time[i][1])

print(cnt)