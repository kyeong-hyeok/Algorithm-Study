# N <= 1,000,000 (100만)
# N*logN < < N^2 -> 완전 탐색?
# 앞 자릿수보다 무조건 작아야 함
# 3자릿수 -> 321 마지막 자리부터 올라가기? 내려오기?

import sys, math
from itertools import combinations
input_data = sys.stdin.readline

N = int(input_data())

result = []
for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        c = list(c)
        c.sort(reverse=True)
        result.append(int("".join(map(str, c))))
result.sort()

try:
    print(result[N])
except:
    print(-1)


# 이전 풀이
# 시간 복잡도를 고려한 더 빠른 방법인데 33%에서 런타임 에러가 뜬다 ,,
# 해당 범위 내에 존재할 때만 combinations list를 구함

d = 1
count = 0
while 1:
    if d >= 10:
        print(-1)
        break
    c = math.comb(10, d)    # 들어갈 수를 고르는 경우의 수
    if count + c < N:
        count += c
        d += 1
    else:
        a = N - count
        b = list(combinations([0,1,2,3,4,5,6,7,8,9], d))
        l = []
        for i in range(len(b)):     # 정렬을 위해 합치는 과정 -> str로 바꿔서 join 하는 방식이 더 좋아 보임
            r = 0
            for j in range(len(b[i])-1, -1, -1):
                r = (r*10) + b[i][j]
            l.append(r)
        l.sort()
        print(l[a])
        break