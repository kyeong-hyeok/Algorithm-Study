import sys
input=sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))

cnt = 0
arr.sort()

for i in range(n):
    l = 0
    r = len(arr)-1

    while (l<r):
        if arr[l]+arr[r] == arr[i]:
            if l == i: # 자기 자신 배제
                l += 1
            elif r == i: # 자기 자신 배제
                r -= 1
            else:
                cnt += 1
                break
        elif arr[l]+arr[r] < arr[i]:
            l += 1
        elif arr[l]+arr[r] > arr[i]:
            r -= 1
print(cnt)

# 투포인터는 0,1 로 시작하는 것과 0,end로 시작하는 2개가 있는데 왜 0,end 로 시작하는걸까!
