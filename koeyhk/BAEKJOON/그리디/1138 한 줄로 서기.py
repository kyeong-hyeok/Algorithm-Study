# 개선한 풀이
# 백트래킹보다 시간 절약 + 메모리 절약
# 그리디
# O(N^2) 40ms로 해결

import sys
input_data = sys.stdin.readline

N = int(input_data())
left = list(map(int, input_data().split()))
line = [0] * N
for i in range(N):      # 키 순서대로 for 문
    cnt = 0
    for j in range(N):      # line을 돌면서 들어가야 하는 위치 확인
        if cnt == left[i] and line[j] == 0:     # 왼쪽에 키 큰 사람 수가 일치하고 아무도 없을 때
            line[j] = i + 1
            break
        elif line[j] == 0:      # 자리가 비어 있다면 자신보다 키 큰 사람 자리이므로 cnt += 1
            cnt += 1

print(*line)


# 이전 풀이
# N = 10 -> 백트래킹
# 자기보다 큰 사람이 왼쪽에 몇 명 있었는지 기억
# 순열로 줄 세운 후 앞과 비교
# 7404ms

import sys
input_data = sys.stdin.readline

N = int(input_data())
left = list(map(int, input_data().split()))
people = []
for i in range(N):
    people.append((i+1, left[i]))
arr = []
visited = [0] * N


def check(ar):
    for i in range(N):
        c = 0
        for j in range(i):
            if ar[i][0] < ar[j][0]:
                c += 1
        if c != ar[i][1]:
            return 0
    return 1


def bt():
    if len(arr) == N:
        if check(arr):
            for i in range(N):
                print(arr[i][0], end=' ')
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(people[i])
            bt()
            arr.pop()
            visited[i] = 0


bt()