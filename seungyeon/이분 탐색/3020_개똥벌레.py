n,m = map(int,input().split())
cave= [[0] * m for _ in range(n)]

# index 홀수이면 아래에서 == 0부터 , 짝수이면 위에서 h-??
for i in range(n):
    num = int(input())
    if i % 2 == 0:  
        for j in range(num): cave[i][j] = 1
    else:
        for j in range(num): cave[i][m-j-1] = 1

vertical = list(zip(*cave))

arr=[]
for i in range(m):
   arr.append(sum(vertical[i]))
arr.sort()

for i in range(len(arr)):
    if arr[i] != arr[i+1] : 
        answer = i+1
        break
print( arr[answer]-1,answer)