# N = 100,000 S = 100,000,000
# O(N)에 수행해야 함

# 놓친 부분
# 길이에 초점을 맞춰, 리스트의 앞부분부터 확인한 후 길이를 늘려 다시 앞부분부터 확인하는 방식으로 진행 -> O(N^2)

# 해결 방법
# s와 e에 초점을 맞춰, e를 증가시키면서 해당 조건을 만족하는 시점이 될 때 s를 증가시키는 방식

# O(N) 문제 풀이
import sys

input_data = sys.stdin.readline
N, S = map(int, input_data().split())
num = list(map(int, input_data().split()))

p = 0
s, e = 0, 0
total = num[0]
result = 1000000000
while s <= e < N:
    if S <= total:
        result = min(e-s+1, result)
        total -= num[s]
        s += 1
    else:
        e += 1
        if e == N:
            break
        total += num[e]

if result != 1000000000:
    print(result)
else:
    print(0)


# O(N^2) 문제 풀이
import sys

input_data = sys.stdin.readline
N, S = map(int, input_data().split())
num = list(map(int, input_data().split()))

p = 0
a = 0

for i in range(N):
    s, e = 0, i
    a += num[i]
    p = 0
    sum_num = a
    for s in range(N-i-1):
        if sum_num >= S:
            p = i+1
            break
        sum_num = sum_num - num[s] + num[s+i+1]
    if sum_num >= S:
        p = i+1
    if p != 0:
        break

print(p)