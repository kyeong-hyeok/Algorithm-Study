import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())
arr = list(map(int,input().split()))

# 같은 정수가 k 개 이하로 포함된 수열의 최장 길이

start,end,answer=0,0,0
cnt = defaultdict(int) # list to dic

while end < n:

    if cnt[arr[end]] >= m: # m보다 큰 숫자였다면 지나가고 cnt -- 해줌 다음에 쓸 수있게
        cnt[arr[start]] -= 1
        start += 1
    else:
        cnt[arr[end]] += 1
        end += 1
        answer = max(answer,end-start) # max 값 갱신
    
print(answer)