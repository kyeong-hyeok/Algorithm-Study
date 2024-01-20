# 첫 문제 풀이
# 해시를 이용해서 이전에 있던 값인지 확인 (O(1)) -> 있던 값이면 인덱스 조사

A, P = map(int, input().split())


def n(x):
    result = 0
    while x > 0:
        a = x % 10
        result += pow(a, P)
        x = x // 10
    return result


i = 1
num = [0] * 100000
num[0] = A
d = dict()
d[A] = 1
while 1:
    num[i] = n(num[i-1])
    if num[i] in d:
        idx = num.index(num[i])
        break
    d[num[i]] = 1
    i += 1

print(idx)


# BFS 문제 풀이
# 방문 여부를 확인하면 되기 때문에 BFS로 해결 가능

from collections import deque

A, P = map(int, input().split())


def n(x):
    result = 0
    while x > 0:
        a = x % 10
        result += pow(a, P)
        x = x // 10
    return result


def bfs(x):
    q = deque()
    q.append(x)
    visited = [0] * 1000000
    visited[x] = 1
    while q:
        x = q.popleft()
        nx = n(x)
        if visited[nx] != 0:
            return visited[nx] - 1
        visited[nx] = visited[x] + 1
        q.append(nx)


print(bfs(A))