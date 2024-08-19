import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
answer=[]

def backTracking(idx):

    if len(answer) == m:
        print(*answer)
        return 


    for i in range(idx,n):
            answer.append(arr[i])
            backTracking(i+1)
            answer.pop()


backTracking(0)