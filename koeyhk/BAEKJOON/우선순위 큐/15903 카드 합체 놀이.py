# n = 1,000, m = 15,000
# x, y번 카드의 값을 x+y(x!=y)로 값 바꿈
# m번 해서 점수 가장 작게 만들기
# 우선순위 큐

import sys
import heapq
input_data = sys.stdin.readline

n, m = map(int, input_data().split())
num = list(map(int, input_data().split()))
heapq.heapify(num)      # O(N)
for i in range(m):
    x = heapq.heappop(num)  # O(logN)
    y = heapq.heappop(num)  # O(logN)
    z = x + y
    heapq.heappush(num, z)  # O(logN)
    heapq.heappush(num, z)  # O(logN)
print(sum(num))