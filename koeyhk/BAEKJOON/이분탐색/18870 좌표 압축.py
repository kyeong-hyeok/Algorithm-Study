# N = 1,000,000

import sys
from bisect import bisect_left
input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))
nu = []     # 중복되지 않은 리스트
di_nu = dict()      # 중복 여부 확인하기 위한 해시
for n in num:
    if n not in di_nu:
        di_nu[n] = 1
        nu.append(n)

sorted_nu = sorted(nu)
for i in range(N):
    # 중복되지 않은 리스트에서 해당 수가 어느 위치에 있는지 확인
    print(bisect_left(sorted_nu, num[i]), end=' ')