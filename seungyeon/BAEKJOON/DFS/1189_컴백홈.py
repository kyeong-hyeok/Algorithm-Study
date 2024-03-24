import sys
input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

r,c,k=map(int,input().split())
arr=[]
for i in range(r):
    arr.append(list(input().rstrip()))


def dfs(x,y,distance):
    global answer
    if x == 0 and y == c-1  and distance ==  k :
        answer += 1

    else:

        arr[x][y] = "T" # 방문처리를 T로 하기 .. 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx < r and 0 <= ny < c and arr[nx][ny] == '.'):
                arr[nx][ny] = 'T'
                dfs(nx,ny,distance+1)
                arr[nx][ny] = '.'
    

answer = 0
dfs(r-1,0,1)
print(answer)