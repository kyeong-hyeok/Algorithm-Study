# k개의 접시 연속해서 먹으면 할인된 정액 가격
# 1번 행사에 참가할 경우 쿠폰에 적혀진 종류의 초밥 하나 무료로 제공 -> 없을 경우 만들어 제공
# 다양한 종류 초밥!
# N = 30,000

# 풀이 아이디어
# 1. count 리스트를 만들어 초밥 종류에 따른 개수를 저장하자!
# count[x]의 값이 0이면 result += 1, count[x] += 1
# count[x]의 값이 0이 아니라면 count[x] += 1

import sys

input_data = sys.stdin.readline

N, d, k, c = map(int, input_data().split())
sushi = [int(input_data()) for _ in range(N)]

count = [0] * 30001
count[c] = 1
result = 1
for i in range(k):      # 0 ~ k-1까지 초밥 count 저장
    if count[sushi[i]] == 0:
        result += 1
    count[sushi[i]] += 1

answer = result
l, r = 0, k-1
while 1:        # O(N)
    l = (l+1) % N
    r = (r+1) % N
    if l == 0:      # 처음 위치로 간 경우 break
        break
    count[sushi[l-1]] -= 1      # 제일 처음 초밥 count 빼기
    if count[sushi[l-1]] == 0:  # count가 0이 됐다면 초밥 종류 감소
        result -= 1
    if count[sushi[r]] == 0:    # 추가되는 초밥의 종류가 없었다면 초밥 종류 증가
        result += 1
    count[sushi[r]] += 1
    answer = max(answer, result)

print(answer)