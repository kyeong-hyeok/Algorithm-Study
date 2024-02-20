# 좀 더 쉬운 접근
# -> 사이클이 생기면 결과값에 포함하기
# -> dfs 시작한 수로 돌아간다면 결과값에 포함

import sys

input_data = sys.stdin.readline

N = int(input_data())
num = [0]
for _ in range(N):
    num.append(int(input_data()))
result_arr = []


def dfs(x, start):
    global result_arr
    if visited[x] == 1:
        if x == start:
            result_arr.extend(list(arr))
        return
    if visited[x] == 0:
        visited[x] = 1
        arr.add(x)
        dfs(num[x], start)


for i in range(1, N+1):
    arr = set()
    visited = [0] * (N + 1)
    dfs(i, i)

result = list(set(result_arr))
print(len(result))
result.sort()
for i in result:
    print(i)


# 이전 풀이
# N = 100
# DFS로 둘째줄 번호가 가리키는 숫자 탐색 -> 이미 방문했으면 멈추기
# 첫째 줄 번호는 arr1에 둘째 줄 번호는 arr2에 저장
# 첫째 줄과 둘째 줄의 번호가 같을 경우 결과값에 더하기


import sys

input_data = sys.stdin.readline

N = int(input_data())
num = [0]
for _ in range(N):
    num.append(int(input_data()))
result_arr = []


def dfs(x):
    global result_arr
    if visited[x] == 1:
        if arr1 == arr2:
            result_arr.extend(list(arr1))
        return
    if visited[x] == 0:
        visited[x] = 1
        arr1.add(x)
        arr2.add(num[x])
        dfs(num[x])


for i in range(1, N+1):
    arr1, arr2 = set(), set()
    visited = [0] * (N + 1)
    dfs(i)

result = list(set(result_arr))
print(len(result))
result.sort()
for i in result:
    print(i)