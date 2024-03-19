# N, K = 1000
# K 국가의 등수만 알면 됨
# O(N) -> 정렬 후 K 국가 찾고 K 앞에서 동점 국가 확인

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
country = [list(map(int, input_data().split())) for _ in range(N)]
country.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(N):
    if country[i][0] == K:
        c = i
        break
result = c+1
for i in range(c-1, -1, -1):
    if country[i][1:] == country[c][1:]:
        result -= 1
    else:
        break
print(result)