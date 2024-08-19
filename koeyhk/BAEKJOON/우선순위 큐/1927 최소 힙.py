# 우선순위 큐

import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data())
q = []
for i in range(N):
    x = int(input_data())
    if x > 0:
        heapq.heappush(q, x)
    elif x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))