# K = 10,000 N = 1,000,000

# 오해한 부분
# 랜선의 길이가 10000이하의 정수라고 착각 . .

import sys

input_data = sys.stdin.readline

K, N = map(int, input_data().split())
length = [int(input_data()) for _ in range(K)]
length.sort()


def able(x):
    result = 0
    for l in length:
        result += l//x
    if result >= N:
        return 1
    return 0


s, e = 1, length[K-1]
result = 0
while s <= e:
    m = (s + e) // 2
    if able(m):
        s = m + 1
    else:
        e = m - 1

print(e)