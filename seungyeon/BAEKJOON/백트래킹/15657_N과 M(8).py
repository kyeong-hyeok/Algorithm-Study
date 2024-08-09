n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()

answer = []

def func(index):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(index,n):
        answer.append(arr[i])
        func(i)
        answer.pop()
         
func(0)

