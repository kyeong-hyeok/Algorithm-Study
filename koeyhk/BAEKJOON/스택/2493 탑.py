# N개의 높이가 서로 다른 탑, 꼭대기 레이저 송신기는 수평 방향으로 왼쪽 발사
# N = 500,000
# 높이마다 가장 오른쪽 열 값 저장 -> 메모리 초과
# 문제 풀이 방법이 생각이 안 난다면 경우를 나눠서 생각해보자!

# 경우를 나눠서 생각해보기
# 1. 현재의 높이보다 스택의 값이 작을 때 -> pop() (현재 들어가는 높이가 가장 오른쪽 최댓값이므로)
# 2. 현재의 높이보다 스택의 값이 클 때 -> 레이저 수신 후 break (인덱스 저장)
# 1, 2번 반복 후 마지막에 stack에 인덱스와 현재의 높이 추가

import sys

input_data = sys.stdin.readline

N = int(input_data())
top = list(map(int, input_data().split()))
stack = []
p = [0] * N
for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:
            p[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append((i, top[i]))

print(*p)
