# N <= 30,000
# d <= 3000 완전 탐색 -> 3000 * 30000 = 90,000,000

import sys

input_data = sys.stdin.readline

N, d, k, c = map(int, input_data().split())
sushi = [int(input_data()) for _ in range(N)]

result = 0
for i in range(len(sushi)):
    count = {c}
    for j in range(i, i+k):
        count.add(sushi[j % N])
    result = max(result, len(count))

print(result)