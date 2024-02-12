# 1~49 중 k개의 수를 가진 집합 S에서 번호 6개 선택

# 문제 풀이 1
# 조합 -> 12C6

import sys
from itertools import combinations

input_data = sys.stdin.readline

while 1:
    S = list(map(int, input_data().split()))
    if S[0] == 0:
        break
    for c in combinations(S[1:], 6):
        print(*c)
    print()


# 문제 풀이 2
# 백트래킹 -> N^6 이하

import sys
input_data = sys.stdin.readline


def bt(x, num):
    if len(arr) == 6:
        print(*arr)
        return
    for i in range(x, len(num)):
        arr.append(num[i])
        bt(i+1, num)
        arr.pop()


while 1:
    S = list(map(int, input_data().split()))
    if S[0] == 0:
        break
    arr = []
    num = S[1:]
    bt(0, num)
    print()