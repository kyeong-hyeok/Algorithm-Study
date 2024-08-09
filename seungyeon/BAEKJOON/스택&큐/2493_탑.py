n=int(input())
arr=list(map(int,input().split()))


answer = [0] * n

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[j] >= arr[i]:
            answer[i] = j+1
            break

print(*answer)