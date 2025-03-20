# import sys
# input=sys.stdin.readline

# n=int(input())

# # 퀸은 위,아래,대각선 상으로 움직일 수 있는 특성
# # 같은 행에 2개 이상의 퀸이 올 수 없음
# # 말 놓는 개수를 하나씩 늘려가며 재귀함수를 호출하다가 이 호출횟수가 n과 같으면 count up 
# # 조건을 만족하지 않으면 이전으로 돌아가 다른 경우를 탐색. 백트래킹

# visited=[-1]*n
# cnt = 0


# def dfs(row):
#     global cnt

#     if row == n:
#         cnt += 1

#     else:
#         for col in range(n):
#             visited[row] = col
#             if check(row):
#                 dfs(row+1)


# def check(now_row):
#     for row in range(now_row):
#         if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row]-visited[row]): # 같은 열, 대각선에 있는지 (행은 visited index로 판별)
#             return False
#     return True

# dfs(0)
# print(cnt)

import sys
input=sys.stdin.readline

n=int(input())

cnt = 0
visited = [-1] * n

def check(now_row):
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row-row == abs(visited[now_row] - visited[row]):
            return False
    return True
    
def dfs(row):

    global cnt 
    if row == n:
        cnt += 1

    else:
        for col in range(n):
            visited[row] = col
            if check(row):
                dfs(row+1)

dfs(0)
print(cnt)

