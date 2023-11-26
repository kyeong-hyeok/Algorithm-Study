# 2 3 5 7
T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())
    s = b - a
    count = 0
    if s == 0:
        count = 0
    elif s <= 1:
        count = -1
    elif s % 2 == 0:
        count = s // 2
    else:
        count = (s - 3) // 2 + 1
    print(f"#{i} {count}")