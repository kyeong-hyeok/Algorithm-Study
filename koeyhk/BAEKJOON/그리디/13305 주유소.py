# N = 100,000
# 앞의 도시 중에서 제일 작은 기름값 저장해두고 필요할 때마다 해당 기름 값으로 보충

import sys

input_data = sys.stdin.readline

N = int(input_data())
distance = list(map(int, input_data().split()))
price = list(map(int, input_data().split()))
total_price = distance[0] * price[0]
for i in range(1, N-1):
    price[i] = min(price[i-1], price[i])
    total_price += price[i] * distance[i]

print(total_price)