# import sys

# input=sys.stdin.readline

# # ij 팀의 능력 = ij+ji
# # 두 팀의 능력치 차이 최소

# n = int(input())
# # i,j 

# arr=[]
# dp=[[0] * n for _ in range(n)]
# for i in range(n):
#     arr_n = list(map(int,input().split()))
#     arr.append(arr_n)
#     # for j in range(len(arr_n)):

# for i in range(n):
#     for j in range(n):
#         dp[i][j] = arr[i][j]+arr[j][i]

# visited=[False]*n
# min_ans=2147000000
# def dfs(idx,cnt):

#     global min_ans

#     if cnt == n//2:

#         team_a_sum,team_b_sum = 0,0
#         team_a,team_b = [],[]

#         # 팀 나누기기
#         for i in range(len(visited)):
#             if visited[i]:
#                 team_a.append(i)
#             else:
#                 team_b.append(i)
#         # 점수 계산산
#         for k in range(len(team_a)-1):
            
#             team_a_sum += dp[team_a[k]][team_a[k+1]]
#             team_b_sum += dp[team_b[k]][team_b[k+1]]

#         team_a_sum += dp[team_a[0]][team_a[-1]]
#         team_b_sum += dp[team_b[0]][team_b[-1]]


#         # 최솟값
#         min_ans=min(abs(team_a_sum-team_b_sum),min_ans)


#     for i in range(idx,n):
#         if not visited[i]:
#             visited[i] = True
#             dfs(i+1,cnt+1)
#             visited[i] = False


# dfs(0,0)
# print(min_ans)
import sys

n=int(input())
arr=[]
for i in range(n):
    arr.append((list(map(int,input().split()))))

visited=[False]*n
min_ans=sys.maxsize
def dfs(idx,cnt):

    global min_ans

    if cnt == n//2:
        # 점수 합산
        sum_a,sum_b = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    sum_a += arr[i][j]
                elif not visited[i] and not visited[j]:
                    sum_b += arr[i][j]
        min_ans = min(min_ans,abs(sum_a-sum_b))

        return 

    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,cnt+1)
            visited[i] = False

dfs(0,0)
print(min_ans)