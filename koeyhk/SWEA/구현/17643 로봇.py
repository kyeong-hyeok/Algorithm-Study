# 27-81

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def isPossible(x, y):
    x = abs(x)
    y = abs(y)
    while x > 0 or y > 0:
        if (x - 1) % 3 == 0 and y % 3 == 0:
            x = (x - 1) // 3
            y = y // 3
        elif (x + 1) % 3 == 0 and y % 3 == 0:
            x = (x + 1) // 3
            y = y // 3
        elif (y + 1) % 3 == 0 and x % 3 == 0:
            y = (y + 1) // 3
            x = x // 3
        elif (y - 1) % 3 == 0 and x % 3 == 0:
            y = (y - 1) // 3
            x = x // 3
        else:
            return 0
    return 1


for i in range(1, T+1):
    x, y = map(int, input().split())
    if isPossible(x, y):
        print(f'#{i} yes')
    else:
        print(f'#{i} no')