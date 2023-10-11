# 1. 원소가 전체 핪의 절반을 넘어가면 안됨
from collections import deque

def solution(queue1,queue2):
    answer = 0

    que1 = deque(queue1)
    que2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if sum1+sum2 %2 != 0:
        return -1

    while True:

        if answer == 2*(len(queue1)+len(queue2)):
            return -1
        
        if sum1 < sum2:
            k = que2.popleft()
            que1.append(k)
            sum2 -= k
            sum1 += k
        elif sum1 > sum2:
            k = que1.popleft()
            que2.append(k)
            sum1 -= k
            sum2 += k
        else:
            return answer
        answer += 1

print(solution([1, 1, 1, 8, 10, 9],[1, 1, 1, 1, 1, 1]))
