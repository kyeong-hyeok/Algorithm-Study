from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    total = q1_sum + q2_sum
    if total % 2 != 0:
        return -1
    i = 0
    while i <= (len(queue1) + len(queue2)) * 2:
        if q1_sum == q2_sum:
            return i
        elif q1_sum > q2_sum:
            num = queue1.popleft()
            queue2.append(num)
            q1_sum -= num
            q2_sum += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            q2_sum -= num
            q1_sum += num
        i += 1
    return -1

