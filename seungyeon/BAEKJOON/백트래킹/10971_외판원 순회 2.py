import sys
input=sys.stdin.readline

n=int(input())
arr= [ list(map(int,input().split())) for _ in range(n) ]
visited=[0]*n
sum=0
answer = sys.maxsize

def dfs(depth,x):
    global sum,answer

    if depth == n-1: # 마지막이고
        if arr[x][0] : # 돌아가는 길에
            sum += arr[x][0] # 값 더하기
            if sum < answer: # 최소값
                answer = sum
            sum -= arr[x][0]
        return
    
    for i in range(1,n):
        if visited[i] == 0 and arr[x][i]:
            visited[i] = 1
            sum += arr[x][i]
            dfs(depth+1,i)
            visited[i] = 0
            sum -= arr[x][i]

dfs(0,0)
print(answer)