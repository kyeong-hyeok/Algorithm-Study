# N = 100,000
# -> O(N^2) 이하로 수행해야 함

import sys

input_data = sys.stdin.readline

N = int(input_data())
numn = list(map(int, input_data().split()))
M = int(input_data())
numm = list(map(int, input_data().split()))
numn.sort()     # O(NlogN)


def bs(x):  # O(MlogN)
    l, r = 0, N-1
    while l <= r:
        m = (l+r)//2
        if numn[m] > x:
            r = m-1
        elif numn[m] < x:
            l = m+1
        else:
            return 1
    return 0


for n in numm:
    print(bs(n))