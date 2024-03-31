# 최대 3000자리

# 문제 접근 방법 -> 구체적으로 생각하지 못함
# num을 1씩 증가시키면서 num과 문자열 비교
# - 첫 자리가 같다면 문자열 첫 자리 지우기
# - num의 다음 수와 s 비교
# s를 다 확인했다면 i 출력

import sys

input_data = sys.stdin.readline

s = input_data().rstrip()

i = 0
while 1:
    i += 1
    num = str(i)
    while num and s:
        if num[0] == s[0]:
            s = s[1:]
        num = num[1:]
    if len(s) == 0:
        print(i)
        break