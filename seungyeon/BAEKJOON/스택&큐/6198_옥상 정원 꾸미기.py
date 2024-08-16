n=int(input())
arr=[]
stack=[]

for i in range(n):
   arr.append(int(input()))

cnt = 0

for i in range(n):

    while stack:

        if arr[i] < stack[-1]:
            cnt += len(stack)
            break
        else :
            stack.pop()


    stack.append(arr[i])

print(cnt)