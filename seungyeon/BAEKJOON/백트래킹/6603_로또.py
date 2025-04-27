import sys
input=sys.stdin.readline

def dfs(idx,cnt,k,sub_arr):

    if cnt == 6:
        print(' '.join(map(str,path)))
        return 

    for i in range(idx,k):
        path.append(sub_arr[i])
        dfs(i+1,cnt+1,k,sub_arr)
        path.pop()

while(True):
    
    arr=list(map(int,input().split()))

    if arr[0] == 0:
        break

    k=arr[0]
    sub_arr=arr[1:]

    path=[]

    dfs(0,0,k,sub_arr)

    print()