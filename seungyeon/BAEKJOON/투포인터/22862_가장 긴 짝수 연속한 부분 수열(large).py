import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr = list(map(int,input().split()))

end,answer,tmp,odd=0,0,0,0

for i in range(n):
    while(odd <= k and end < n):
        if arr[end]%2:
            odd += 1
        else:
            tmp += 1
        end += 1

        if i == 0 and end == n:
            answer = tmp
            break
    if odd == k+1:
        answer = max(tmp,answer)
    if arr[ii] % 2:
        odd -= 1
    else: 
        tmp -= 1

print(answer)