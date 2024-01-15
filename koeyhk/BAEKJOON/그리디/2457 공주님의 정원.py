# 문제 풀이 시 생각한 것!
# N개의 꽃
# 3월 1일부터 11월 30일까지 꽃이 한 가지 이상 피어 있기
# 심는 꽃의 개수의 최솟값
# N = 100,000 -> O(N^2) 이하
# 월 -> 일로 생각 = 31 * 5 + 4 * 30 = 275

# 풀이의 효율성 높이기
# 1. 월에 100을 곱하고 일을 더해서 date 리스트를 만들면 월 일이 서로 영향이 안 받음

# 접근 방법
# 1. 월 일을 date로 바꿈 -> O
# 2. date를 시작 날짜 순으로 정렬 -> O
# 3. date에 따라 마지막 꽃이 지는 날짜를 갱신하고 원소 삭제 -> X

# 생각하지 못한 부분
# 3. 정렬된 순서에 따라 현재 꽃의 시작 날짜가 마지막 꽃이 지는 날짜보다 이전일 때
# -> 제일 늦게 지는 꽃을 찾기 (확인한 꽃은 지움)


import sys

input_data = sys.stdin.readline

N = int(input_data())
date = []
for i in range(N):
    a, b, c, d = map(int, input_data().split())
    date.append([a*100+b, c*100+d])

date.sort()
e = 301
result = 0
while date:
    # 마지막 꽃이 지는 날짜가 12월 1일 이상이거나
    # 확인할 꽃의 시작 날짜가 마지막 꽃의 지는 날짜와 이어지지 않는 경우
    if e >= 1201 or date[0][0] > e:
        break
    max_e = -1
    for _ in range(len(date)):
        if date[0][0] <= e:     # 꽃이 피는 날짜가 e 이전일 때
            if max_e <= date[0][1]:     # 가장 느리게 지는 꽃 확인
                max_e = date[0][1]
            date.remove(date[0])
        else:
            break
    e = max_e       # e 갱신
    result += 1

if e < 1201:
    print(0)
else:
    print(result)
