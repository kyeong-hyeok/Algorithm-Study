# 대각선 왼쪽 [i+1][j-1]
# 대각선 오른쪽 [i+1][j+1]
# 합이 최대가 되는 경로에 있는 수의 합


import sys
input=sys.stdin.readline

arr=[]
n=int(input())
for i in range(n):
    arr.append( list(map(int,input().split())))

for i in range(1,n): # 1번부터 
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j==i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1],arr[i-1][j])

print(max(arr[n-1]))
# def dfs(x,y,depth,cnt):

#     if depth == n:
#         print(cnt)
#         return cnt
    
#     cnt += arr[x][y]

#     if arr[x+1][y-1] < arr[x+1][y+1]:
#         nx,ny=x+1,y+1
#     else:
#         nx,ny=x+1,y-1
#     if 0 < nx and nx < n and 0 < ny and ny < n:
#         dfs(nx,ny,depth+1,cnt)


# dfs(0,0,0,0)