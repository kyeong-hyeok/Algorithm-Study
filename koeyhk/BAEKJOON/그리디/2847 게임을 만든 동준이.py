# 레벨 난이도 순으로 배치 -> 하지만 쉬운 레벨 점수 높은 경우 있음
# 각 레벨을 클리어할 때 점수 증가하도록 만들려고 함
# 몇 번 감소 시키면 되나?

# 탐욕법
# (마지막 레벨 - 1)의 점수부터 첫 번째 레벨의 점수가 다음 레벨보다 작아야 함

import sys

input_data = sys.stdin.readline

N = int(input_data())
score = [int(input_data()) for _ in range(N)]
result = 0
for i in range(N-2, -1, -1):
    k = score[i] - score[i+1]
    if k >= 0:
        result += k + 1
        score[i] = score[i+1] - 1

print(result)