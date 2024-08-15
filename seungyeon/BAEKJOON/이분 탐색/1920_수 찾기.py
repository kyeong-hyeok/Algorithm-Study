n=int(input())
a=list(map(int,input().split(" ")))
a.sort()

m=int(input())
arr=list(map(int,input().split(" ")))


def binary(k):

    l = 0
    r = n-1

    while(l <= r):
        mid = (l+r) // 2

        if k > a[mid]:
            l = mid + 1
        elif k < a[mid]:
            r = mid - 1
        else:
            l = mid
            r = mid
            break

    if l == mid and r == mid:
        print(1)
    else:
        print(0)


            

for i in range(len(arr)):
    binary(arr[i])


# n=int(input())
# a=set(map(int,input().split(" ")))
# m=int(input())
# arr=list(map(int,input().split(" ")))

# for i in arr:
#     if i not in a:
#         print('0')
#     else:
#         print('1')