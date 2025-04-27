import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=dict()
arr_reverse = dict()
for i in range(1,n+1):
   k = input().rstrip()
   arr[str(i)] = k
   arr_reverse[k] = str(i)

for i in range(m):
    # 알파벳 -> 번호 
    # 숫자 -> 문자 
    str = input().strip()

    if str.isdigit():
        print(arr[str])
    else:
        print(arr_reverse[str])