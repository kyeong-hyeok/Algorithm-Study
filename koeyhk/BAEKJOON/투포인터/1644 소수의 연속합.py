# N = 4,000,000
# O(N)에 수행 -> 투포인터

N = int(input())

# 소수 구하기 - 에라토스테네스의 체
# 시간 복잡도 6608ms -> 768ms

a = [False, False] + [True] * (N+1)
prime = []

for i in range(2, N+1):
    if a[i]:
        prime.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

if N < 2:
    print(0)
    exit()

s, e, cnt = 0, 0, 0
total = prime[0]
while s <= e < N:
    if total >= N:
        if total == N:
            cnt += 1
        total -= prime[s]
        s += 1
    else:
        e += 1
        if e >= len(prime):
            break
        total += prime[e]

print(cnt)



# 이전 소수 찾기 코드

import math


def isPrime(x):
    n = int(math.sqrt(x))
    for i in range(2, n+1):
        if x % i == 0:
            return 0
    return 1
prime = []
for i in range(2, N+1):
    if isPrime(i):
        prime.append(i)