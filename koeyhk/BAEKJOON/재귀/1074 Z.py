# 완전 탐색 2^15 불가능
# 사분면으로 나누기 -> 재귀

n, r, c = map(int, input().split())
result = 0


def search(x, y, n):
    global result
    if x == r and y == c:
        print(result)
        exit(0)
    if n == 1:
        result += 1
        return
    if not (x <= r < x+n and y <= c < y+n):
        result += n*n
        return
    nn = n//2
    search(x, y, nn)
    search(x, y+nn, nn)
    search(x+nn, y, nn)
    search(x+nn, y+nn, nn)


search(0, 0, 2**n)
print(result)