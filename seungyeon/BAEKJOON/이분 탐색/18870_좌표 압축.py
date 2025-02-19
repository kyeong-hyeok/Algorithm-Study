import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
arr2=sorted(set(arr))

# 배열을 한번 순회하면서 이분탐색으로 하나씩 위치를 찾는다 (나 보다 작은 값이 몇개인지)
result =[]
for i in range(n):
    start,end=0,len(arr2)-1

    while start <= end:
        mid = (start+end)//2

        if arr2[mid] < arr[i]:
            start = mid + 1
        elif arr2[mid] > arr[i] :
            end = mid - 1
        else:
            result.append(str(mid))
            break
print(' '.join(result))