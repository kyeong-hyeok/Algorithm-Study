# 버틸 수 있는 최대 중량이 큰 로프부터 걸릴 수 있는 최대 중량 확인하기
import sys

input_data = sys.stdin.readline

N = int(input_data())
rope = [int(input_data()) for _ in range(N)]
rope.sort(reverse=True)
max_w = rope[0]
for i in range(1, len(rope)):
    max_w = max(max_w, rope[i] * (i+1))

print(max_w)