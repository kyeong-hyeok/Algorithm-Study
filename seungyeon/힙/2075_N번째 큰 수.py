import heapq

heap = []
n = int(input())

for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n:
            heapq.heappush(heap, number)
        else:
            if heap[0] < number: # 값 갱신
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0]) # n만큼 크기의 heap 중 가장 작은 것 = n번째 큰 수
