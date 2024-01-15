import sys
input = sys.stdin.readline

n,m=map(int,input().split())
visited=[False]*(10001)
arr = list(map(int,input().split()))
answer =[]
arr.sort()

def dfs(depth):
    if depth==m:
        print(' '.join(map(str,answer)))
        return 
    
    for i in arr:
        if visited[i] == False :
            visited[i] = True
            answer.append(i)
            dfs(depth+1)
            visited[i] = False
            answer.pop()

dfs(0)
