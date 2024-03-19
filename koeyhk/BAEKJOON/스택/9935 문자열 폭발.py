# 모든 폭발 문자열 폭발 -> 남은 문자열 이어붙임
# 새로 생긴 문자열에도 폭발 확인
# 폭발 문자열은 같은 문자 중복 x
# N = 1,000,000

# 생각하지 못한 것
# 문자열을 지우고 앞으로 이동할 필요없이 stack을 사용해서 현재 들어온 문자에 따라 비교
# 폭발 문자열은 같은 문자 중복되지 않기 때문!!

# 잘못된 비교
# 문자열과 리스트 비교 x -> 리스트를 문자열로 바꾸거나 문자열을 리스트로 바꿔야함

import sys

input_data = sys.stdin.readline

str = input_data().rstrip()
bomb_str = input_data().rstrip()
b = len(bomb_str)
stack = []
for i in str:
    stack.append(i)
    if i == bomb_str[-1] and ''.join(stack[len(stack)-b:]) == bomb_str:
        for _ in range(b):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")