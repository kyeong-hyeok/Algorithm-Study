import sys
input=sys.stdin.readline



arr=[0] * (101)

arr[0] = 0
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2

for i in range(5,101):
    arr[i] = arr[i-2]+arr[i-3]



t=int(input())
for _ in range(t):
    n=int(input())
    print(arr[n])