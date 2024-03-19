N, M = map(int, input().split())
visited = [0] * (N+1)
arr = []


def bt():
    if len(arr) == M:
        for a in arr:
            print(a, end=' ')
        print()
        return
    for i in range(1, N+1):
        visited[i] = 1
        arr.append(i)
        bt()
        arr.pop()
        visited[i] = 0


bt()