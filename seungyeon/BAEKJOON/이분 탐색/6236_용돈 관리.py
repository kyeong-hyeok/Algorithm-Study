import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append((int(input())))

start = min(arr)
end = sum(arr)

while start <= end:
    mid = (start+end)//2

    money = mid
    cnt = 1

    for i in arr:
        if money - i < 0 : # 꺼낸돈보다 쓸 돈이 부족함
            money = mid # 다시 충전
            cnt += 1

        money -= i # 사용

    if cnt > m or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)