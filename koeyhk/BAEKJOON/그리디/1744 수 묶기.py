# N = 50
# 제일 작은 음수부터 두 개씩 곱한 값, 나머지
# 제일 큰 양수부터 두 개씩 곱한 값, 나머지
# 1은 그냥 더하기

import sys

input_data = sys.stdin.readline

N = int(input_data())
plus = []
minus = []
result = 0

for _ in range(N):
    num = int(input_data())
    if num > 1:
        plus.append(num)
    elif num == 1:
        result += 1
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += plus[i] * plus[i+1]

for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += minus[i] * minus[i+1]

print(result)