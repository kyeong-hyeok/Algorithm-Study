from math import gcd


def solution(a, b):
    b //= gcd(a, b)
    while b % 2 == 0:
        b /= 2
    while b % 5 == 0:
        b /= 5
    return 1 if b == 1 else 2


T = int(input())
for i in range(T):
    n = int(input())
    S = list(map(int, input().split()))
    total = sum(S)
    answer = total/n
    if solution(total, n) == 1:
        print('#'+str(i+1), "%g" %(round(answer, 20)))
    else:
        print('#'+str(i+1), format(answer, ".20f"))
