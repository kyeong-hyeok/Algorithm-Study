# N, M = 1000

# 첫 번째 풀이
# n개의 포인터로 최솟값을 가지는 값의 포인터를 하나씩 증가하면서 최대 최소 구함
# 투 포인터 + 리스트 사용

import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
cl = [list(map(int, input_data().split())) for _ in range(N)]
for c in cl:
    c.sort()

pointer = [0] * (N+1)
arr = []
mi = 10e9
ma = 0
for c in cl:
    arr.append(c[0])
    mi = min(mi, c[0])
    ma = max(ma, c[0])
result = ma - mi

# 시간 복잡도 = O(N) * O(N^2)
while 1:
    a = arr.index(mi)
    if pointer[a] > M-2:
        break
    pointer[a] += 1
    arr[a] = cl[a][pointer[a]]
    mi = min(arr)
    ma = max(arr[a], ma)
    result = min(result, ma-mi)

print(result)


# 두 번째 풀이
# 투 포인터 + 우선순위 큐 사용 -> 최솟값, 최댓값 구할 때 N -> logN 단축

import sys
import heapq

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
cl = [list(map(int, input_data().split())) for _ in range(N)]
for c in cl:
    c.sort()

pointer = [0] * (N+1)
arr = []
mi = 10e9
ma = 0
for i in range(N):
    heapq.heappush(arr, (cl[i][0], i))  # O(logN)
    mi = min(mi, cl[i][0])
    ma = max(ma, cl[i][0])
result = ma - mi

# 시간 복잡도 = O(logN) * O(N^2)
while 1:
    k, i = heapq.heappop(arr)   # O(logN)
    if pointer[i] > M - 2:
        break
    pointer[i] += 1
    heapq.heappush(arr, (cl[i][pointer[i]], i))     # O(logN)
    mi = arr[0][0]
    ma = max(ma, cl[i][pointer[i]])
    result = min(result, ma-mi)

print(result)