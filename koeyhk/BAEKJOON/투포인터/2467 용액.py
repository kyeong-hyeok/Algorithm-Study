import sys

input_data = sys.stdin.readline

N = int(input_data())
water = list(map(int, input_data().split()))
l, r = 0, N-1
result = sys.maxsize

while l < r:
    diff = water[l] + water[r]
    if abs(diff) < result:
        result = abs(diff)
        o, t = water[l], water[r]
    if diff < 0:
        l += 1
    elif diff > 0:
        r -= 1
    else:
        break

print(o, t)