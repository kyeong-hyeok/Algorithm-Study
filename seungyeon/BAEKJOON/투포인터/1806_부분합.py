# r이 s 이상 이 되는 값을 찾고 
# l이 길이를 좁힌다

# []] 0
# [5] 5
# [5, 1] 6
# [5, 1, 3] 9
# [5, 1, 3, 5] 14
# [5, 1, 3, 5, 10] 24 -> 이상 되는 값 찾고
# [1, 3, 5, 10] 19
# [3, 5, 10] 18
# [5, 10] 15 -> 줄여나가기 . min_length 도 2로 갱신
# [10] 10
# [10, 7] 17
# [7] 7
# [7, 4] 11
# [7, 4, 9] 20
# [4, 9] 13
# [4, 9, 2] 15
# [9, 2] 11
# [9, 2, 8] 19
# [2, 8] 10

import sys
input=sys.stdin.readline

n,s=map(int,input().split())

arr=list(map(int,input().split()))

l,r=0,0
answer,sum = 1e9,0
k = []

while(True):
    if sum >= s:
        answer = min(answer,r-l)
        sum -= arr[l]
        k.remove(arr[l])
        l += 1

    elif r == n:
        break
    
    else:
        sum += arr[r]
        k.append(arr[r])
        r+=1

if answer == 1e9:
    print(0)
else:
    print(answer)

