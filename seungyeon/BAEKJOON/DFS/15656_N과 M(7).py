import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))

# 각 원소 중복 사용 가능
answer = []

def dfs(k):

    if k == m:
        print(' '.join(map(str,answer)))
        return 
    
    for i in arr:
        answer.append(i)
        dfs(k+1)
        answer.pop()

dfs(0)
