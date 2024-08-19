import sys,heapq

input=sys.stdin.readline

n,m = map(int,input().split(" "))
arr=list(map(int,input().split(" ")))


arr.sort()

pos = []
neg = []

largest = max(max(arr) , -min(arr))

# 최소 힙을 위해 원소를 음수로 구성 
# 최대 힙(max heap)은 부모 노드의 키 값이 자식 노드의 키값보다 크거나 같은 완전 이진 트리이고,
# 최소 힙(min heap)은 부모 노드의 키 값이 자식 노드의 키값보다 작거나 같은 완전 이진트리입니다.

# heapq는 최소힙이니까 양수도 처리하려면 양수에다가 음수를 곱해서 1,10 있을 때 원래라면 1을 뽑는데 -1,-10 하면 -10 뽑으니까 

for i in arr:
    if i > 0:
        heapq.heappush(pos,-i)
    else :
        heapq.heappush(neg,i)

result = 0

while pos:
    result += heapq.heappop(pos)
    for i in range(m-1):
        if pos:
            heapq.heappop(pos)

while neg:
    result += heapq.heappop(neg)
    for i in range(m-1):
        if neg:
            heapq.heappop(neg)

print(-result * 2 - largest)

## 우선순위 큐
### 가장 먼 책을 마지막으로 
### 왕복거리 - 가장 먼 책의 편도거리
