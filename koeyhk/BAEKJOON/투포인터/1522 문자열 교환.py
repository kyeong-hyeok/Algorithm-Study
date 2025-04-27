# a를 모두 연속으로 만들기 -> 교환수 최소로
# 처음과 끝 인접
# 가운데로 옮기기, 양 끝으로 옮기기?
# N = 1,000

# 생각하지 못한 접근
# a가 모두 연속되어야 하므로 a의 개수를 슬라이딩 윈도우로 두고 그 안에서 b의 개수를 찾으면 교환의 최솟값
# 원형이기 때문에 a의 개수만큼 문자열 첫 부분을 뒤에 더해줌!

import sys

input_data = sys.stdin.readline

s = list(input_data().rstrip())
a_cnt = s.count('a')
s += s[:a_cnt]
result = 1000
for i in range(len(s)-a_cnt):
    result = min(result, s[i:i+a_cnt].count('b'))
print(result)