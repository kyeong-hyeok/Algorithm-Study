n,m=map(int,input().split())

answer = []
visited=[0] * ( n + 1)


def dfs(depth):

    if depth == m:
        print(*answer)
        return
    
    for i in range(1,n+1):

        if visited[i] == 0:
            answer.append(i)
            visited[i] = 1
            dfs(depth+1)
            visited[i] = 0
            answer.pop()
    

dfs(0)