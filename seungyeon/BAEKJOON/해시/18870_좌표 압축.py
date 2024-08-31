import sys
input = sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))

s = sorted(list(set(arr))) # 중복제거 

dic = dict()
for i in range(len(s)):
    dic[s[i]] = i

for i in arr:
    print(dic[i], end = ' ')
