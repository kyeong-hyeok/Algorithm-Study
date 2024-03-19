# N = 1,000 개로 이루어진 집합 U -> 세 수의 합 d가 U 안에 포함되는 가장 큰 d
# 2 3 5 10 18

# 문제에서 놓친 부분
# x + y + z = k -> x + y = k - z
# x + y를 집합안에 넣고 k-z와 같은지 큰 수부터 비교하면 답


import sys

input_data = sys.stdin.readline

N = int(input_data())
U = list(int(input_data()) for _ in range(N))
U.sort()

U_s = set()
for i in U:
    for j in U:
        U_s.add(i+j)


for i in range(N-1, -1, -1):
    for j in range(i+1):
        if U[i] - U[j] in U_s:
            print(U[i])
            exit()



# 실패한 풀이
# 마지막 한 개의 수를 이분 탐색으로 구하면 되지 않을까? -> 오답


import sys

input_data = sys.stdin.readline

N = int(input_data())
U = list(int(input_data()) for _ in range(N))
U.sort()
d = dict()
for i in U:
    d[i] = 1


def bs(x, y):
    result = U[x] + U[y]
    l, r = 0, N-1
    a = 0
    while l <= r:
        m = (l+r) // 2
        if U[m] < result:
            l = m+1
        else:
            r = m-1
            if (U[m] - result) in d:
                a = U[m]
    return a



for i in range(N-2, -1, -1):
    for j in range(i, -1, -1):
        if U[i] + U[j] < U[N-1]:
            a = bs(i, j)
            if a != 0:
                print(a)
                exit()