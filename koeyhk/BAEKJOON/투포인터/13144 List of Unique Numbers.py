# 25
# N = 100,000
# 연속한 1개 이상의 수를 뽑았을 때 같은 수 x 경우의 수
# 1 -> + 1
# 1 2, 2 -> + 2
# 2 3, 3, 1 2 3 -> + 3
# 3, 4, 2 3 4, 1 2 3 4 -> + 4 (e-s+1)

# 정확한 해결책을 정해놓지 않고 시작함 -> 풀이를 여러 번 바꾸게 됨!! ㅜ

# 풀이
# 시작: s, 끝: e

# 1. num[e]가 중복되지 않는 경우
# (e-s+1)만큼 경우의 수 증가시킴 (문제 예제를 통해 규칙 확인)

# 2. num[e]가 중복되는 경우
# a = num[e]와 같은 값의 인덱스
# a+1, e까지 해시에 추가한 후 (e-s+1)만큼 경우의 수를 증가시킴

import sys

input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))

s, e = 0, 1
n = dict()
n[num[0]] = 0
result = 1
while s <= e < N:
    if num[e] not in n:
        n[num[e]] = e
        result += (e-s+1)
        e += 1
    else:
        a = n.get(num[e])
        s = a+1
        n = dict()
        for i in range(a+1, e+1):
            n[num[i]] = i
        result += (e-s+1)
        e += 1

print(result)

# 생각했던 다른 방법 -> 더 쉬움!
# N 크기만큼의 리스트 -> 해당 수의 존재 여부 확인

# 구현이 어려울 것이라 생각했던 부분
# 현재 수(num[e])가 중복될 경우 이전에 해당 값을 가진 수 다음부터 수열을 구성해야 하는데 어렵지 않을까?
# 해결책 - 단순히 n[num[s]] = 0으로 두고 s만 늘려주면 된다! -> num[e]가 중복되지 않을 때까지 s가 증가하기 때문이다.

import sys

input_data = sys.stdin.readline

N = int(input_data())
num = list(map(int, input_data().split()))

s, e = 0, 0
n = [0] * 100001
result = 0
while s <= e < N:
    if n[num[e]] == 0:
        n[num[e]] = 1
        e += 1
        result += (e-s)
    else:
        n[num[s]] = 0
        s += 1

print(result)