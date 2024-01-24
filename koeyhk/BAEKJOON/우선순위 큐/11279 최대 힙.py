# 자연수 x 넣기 -> 큰 값 출력 후 제거

import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data())
q = []
for i in range(N):
    x = int(input_data())
    if x > 0:
        heapq.heappush(q, (-x, x))
    else:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])