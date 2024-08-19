import sys
import copy
input=sys.stdin.readline
n,m=map(int,input().split())

cctv=[]
arr=[]

mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[1,2,3],[0,2,3],[0,1,3]],
    [[0,1,2,3],]
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]


for i in range(n):
    data=list(map(int,input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])

def fill(board,mode,x,y):
    for i in mode:
        nx=x
        ny=y

        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break

            if arr[nx][ny] == 6:
                break

            elif arr[nx][ny] == 0:
                arr[nx][ny] = -1


def dfs(depth,board):
    global min_value

    if depth == len(cctv):
        count = 0

        for i in range(n):
            count += board[i].count(0)

        min_value=min(min_value,count)
        return 
    
    tmp = copy.deepcopy(arr)
    cctv_num,x,y = cctv[depth]
    for i in mode[cctv_num]:
        fill(tmp,i,x,y)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)

min_value = int(1e9)
dfs(0,arr)
print(min_value)