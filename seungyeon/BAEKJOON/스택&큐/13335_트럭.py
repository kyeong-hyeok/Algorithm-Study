import sys
input = sys.stdin.readline

from collections import deque
deq = deque()

n, w, l = map(int, input().split()) # W : 다리 길이 , L : 다리 하중 
arr = list(map(int, input().split()))

for _ in range(w) :
    deq.append(0)

now = 0 # 현재 다리 위의 무게
count = 0

while len(arr) > 0 :
    truck = arr[0]

    check = deq.popleft()

    if check != 0 :
        now -= check

    if (now + truck) <= l :
        
        deq.append(truck)
        now += truck
        
        count += 1
        arr.pop(0)
    
    else :
        deq.append(0)

        count += 1

while len(deq) > 0 :
    deq.popleft()
    count += 1

print(count)