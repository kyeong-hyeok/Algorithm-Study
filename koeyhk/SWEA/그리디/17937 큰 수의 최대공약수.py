T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    # 같다면 해당 수 반환, 다르다면 1 반환
    p = A if A == B else 1
    print(f"#{i} {p}")


# 첫 코드 - 서로소는 범위 10 내에 하나 이상 존재한다고 생각했음

import math

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    g = A
    for j in range(A+1, B+1):
        if j > A+10:
            break
        g = math.gcd(j, g)
    print(f"#{i} {g}")