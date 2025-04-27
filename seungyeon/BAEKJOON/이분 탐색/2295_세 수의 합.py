# # 집합안에 포함되는 세수의 합인데 가장 큰거 

# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(int(input().rstrip()))

# l,r=0,0
# sum=0
# arr_set=set(arr)

# answer=[]
# while(True):

#     if r >n-1 or l >r : 
#         break
    
#     if sum == arr[r]:
#         answer.append(sum)
#         sum -= arr[l]
#         l += 1
    
 
#     sum += arr[r]
#     r+= 1

# answer.sort()

# if n==0:
#     print(0)
# else:
#     print(answer[-1])



import sys
input=sys.stdin.readline

answer = 0
n = int(input())
arr=[int(input()) for _ in range(n)]

arr.sort()
arr2=list()

for i in range(n):
    for j in range(i,n):
        arr2.append(arr[i]+arr[j])

print(arr2)
arr2.sort()

for i in range(n):
    for j in range(i,n):
        num = arr[j] - arr[i]
        start = 0
        end = len(arr2) - 1


        while start <= end:
            mid = (start+end)//2

            if num > arr2[mid]:
                start = mid + 1
            elif num < arr2[mid]:
                end = mid-1
            else:
                answer=max(answer,arr[j])
                break

print(answer)
