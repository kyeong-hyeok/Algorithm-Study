# 주식 하나 사기 or 원하는 만큼 주식 팔기 or 가만히 있기
# N = 1,000,000 -> O(N)

# 문제 풀이 아이디어 -> 그리디
# 마지막부터 한 바퀴 돌면서 현재(i)의 다음값들(i+1 ~ N-1) 중 최댓값 저장

# 코드 개선
# 1. max_price를 리스트로 만들지 않고 값으로 갱신 (for문 하나)

import sys

input_data = sys.stdin.readline

T = int(input_data())
for _ in range(T):
    N = int(input_data())
    price = list(map(int, input_data().split()))
    max_price = price[N-1]
    result = 0
    for i in range(N-2, -1, -1):
        if price[i] < max_price:
            result += max_price - price[i]
        else:
            max_price = price[i]
    print(result)
