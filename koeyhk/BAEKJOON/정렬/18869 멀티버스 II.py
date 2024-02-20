# 집합, 딕셔너리, 튜플을 이용한 문제 풀이 648ms

# 생각하지 못 했던 방법
# 1. 중복되는 값은 set으로 제거
# 2. 행성에 대한 순위를 rank[행성] = 순위 로 저장
# 3. tuple로 인덱스에 따른 순위 저장

import sys
import math

input_data = sys.stdin.readline

M, N = map(int, input_data().split())
universe = dict()
for _ in range(M):
    u = list(map(int, input_data().split()))
    u_sort = sorted(list(set(u)))
    rank = {u_sort[i] : i for i in range(len(u_sort))}
    t = tuple([rank[i] for i in u])
    try:
        universe[t] += 1
    except:
        universe[t] = 1
result = 0
for v in universe.values():
    if v >= 2:
        result += math.comb(v, 2)
print(result)


# 이전 풀이
# 딕셔너리 + 문자열 1996ms

# 디버깅
# 40 10 10, 30 10 20 인 경우 쌍으로 성립할 수 없다는 것을 놓침!
# 이전 값과 같은 값일 때 문자열에 '100002'를 더해주기

import sys
import math

input_data = sys.stdin.readline

M, N = map(int, input_data().split())
universe = [list(map(int, input_data().split())) for _ in range(M)]
uni_dict = dict()
for u in universe:
    uni = []
    for i in range(N):
        uni.append((i, u[i]))
    uni.sort(key=lambda x: x[1])
    r = ''
    for i in range(N):
        r += str(uni[i][0])
        if uni[i-1][1] == uni[i][1]:
            r += '100002'
    try:
        uni_dict[r] += 1
    except:
        uni_dict[r] = 1
result = 0
for k, v in uni_dict.items():
    if v >= 2:
        result += math.comb(v, 2)
print(result)