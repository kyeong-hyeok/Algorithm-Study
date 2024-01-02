# 수열을 저장할 배열 ans
# 경우의 수 result

# 탐색 조건: 중복 제외
# 탐색 종료 조건: 부분 수열의 합 = S

import sys

input_data = sys.stdin.readline

N, S = map(int, input_data().split())
num = list(map(int, input_data().split()))
ans = []
result = 0


def bt(x):
    global result
    if sum(ans) == S and len(ans) > 0:
        result += 1
    for i in range(x, N):
        ans.append(num[i])
        bt(i+1)
        ans.pop()


bt(0)
print(result)