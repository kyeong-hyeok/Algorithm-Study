import heapq
import sys

input_data = sys.stdin.readline

N = int(input_data())
chart = []
min_heap = []
for i in range(N):
    chart = list(map(int, input_data().split()))
    for j in chart:
        heapq.heappush(min_heap, j)
        if i > 0:
            heapq.heappop(min_heap)
print(heapq.heappop(min_heap))
