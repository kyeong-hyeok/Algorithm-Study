# 잘못 생각한 부분
# 1. 그래프 문제라고 생각해 find_parent(x) 함수를 만들었다
# -> 방향 그래프이기 때문에 빙빙 돌 수밖에 없음
# 따라서 dfs로 방문하고 visited[x] = 1로 바꾸면 된다!

# 문제 푸는 방식이 잘못된 것을 빨리 인지하는 것이 중요하다!
# 싸이클 -> 그래프 문제 아닐 수도 있음

import sys
sys.setrecursionlimit(10**7)

input_data = sys.stdin.readline
T = int(input_data())


def dfs(x):
    if visited[x] != 0:
        return 0
    visited[x] = 1
    dfs(num[x-1])
    return 1


for i in range(T):
    N = int(input_data())
    num = list(map(int, input_data().split()))
    visited = [0] * (N+1)
    result = 0
    for j in range(1, N+1):
        if dfs(j) == 1:
            result += 1
    print(result)