n = int(input())

arr=list(map(int,input().split(" ")))
x = int(input())

arr.sort()

l,r = 0,len(arr)-1
cnt = 0

while (True):

    if l >= r:
        print(cnt)
        break
    
    if arr[l] + arr[r] == x:
        cnt += 1
        l += 1
        r -= 1
    
    elif arr[l] + arr[r] > x:
        r -= 1
    
    elif arr[l] + arr[r] < x :
        l += 1
    