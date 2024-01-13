# 최대 K번 삭제한 수열에서 짝수로 이루어진 연속한 부분 수열 중 가장 긴 길이?
# N = 1,000,000 K = 100,000

# 놓친 부분
# 투포인터 -> s, e 증가시키면서 최댓값 구하기
# O(N) + O(K)

import sys

input_data = sys.stdin.readline

N, K = map(int, input_data().split())
num = list(map(int, input_data().split()))

e, result, tmp, count = 0, 0, 0, 0
for s in range(N):
    while (count <= K and e < N):
        if num[e] % 2:      # 홀수 -> count += 1
            count += 1
        else:               # 짝수 -> tmp += 1 (부분 수열 길이)
            tmp += 1
        e += 1
        if s == 0 and e == N:
            result = tmp
            break
    result = max(result, tmp)
    if num[s] % 2:      # start 값이 홀수 -> count -= 1
        count -= 1
    else:               # start 값이 짝수 -> tmp -= 1
        tmp -= 1

print(result)
