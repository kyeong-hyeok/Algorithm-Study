import copy

arr=[]
cctv=[]

n,m = map(int,input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

for i in range(n):
    data = list(map(int,input().split()))
    arr.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])

def watch(x,y,arr,hi): # 
    for i in hi: # direction
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = '#'

def dfs(depth ,arr): # 모든 cctv 
    global answer

    if depth == len(cctv):
        count = 0
        for i in range(n):
            count  += arr[i].count(0)
        answer = min(answer,count)
        return 
    
    tmp = copy.deepcopy(arr)
    cctvs,x,y = cctv[depth]

    for i in direction[cctvs]: 
        watch(x,y,tmp,i)
        dfs(depth+1,tmp)
        tmp = copy.deepcopy(arr)

answer = int(1e9) # 최소값
dfs(0,arr)
print(answer)
