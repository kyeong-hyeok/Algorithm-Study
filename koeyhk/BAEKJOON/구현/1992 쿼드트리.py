import sys

input_data = sys.stdin.readline

N = int(input_data())
S = [list(map(int, input_data().strip())) for i in range(N)]


def quad(x, y, z):
    q = 1
    for i in range(x, x+z):
        for j in range(y, y+z):
            if S[x][y] != S[i][j]:
                q = 0
                break
    if q == 1:
        if S[x][y] == 1:
            print(1, end='')
        else:
            print(0, end='')
    else:
        print("(", end='')
        z = z // 2
        quad(x, y, z)
        quad(x, y+z, z)
        quad(x+z, y, z)
        quad(x+z, y+z, z)
        print(")", end='')


quad(0, 0, N)