# N = 200,000 K = 100 -> O(N^2) 미만
# 투포인터 -> K개 이상이 될 때 l 증가

# 개선할 수 있었던 부분
# 1. 해시 -> count 리스트로 해당 수의 개수 저장
# 2. cnt 변수를 따로 만들어 길이를 구하지 않고 수열의 길이를 r-l로 구함

import sys

input_data = sys.stdin.readline
N, K = map(int, input_data().split())
num = list(map(int, input_data().split()))

result, l, r = 0, 0, 0
count = [0] * 100001

while l <= r < N:
    if count[num[r]] < K:
        count[num[r]] += 1
        r += 1
        result = max(r - l, result)
    else:
        count[num[l]] -= 1
        l += 1

print(result)