import sys
input=sys.stdin.readline

def recur(sum,sign,num,n,string):
    if (n == k):
        sum = sum + (sign*num)
        if sum == 0:
            print(string)
    else:
        recur(sum,sign,num*10+(n+1),n+1,string+' '+str(n+1))
        recur(sum+sign*num,1,(n+1),n+1,string+'+'+str(n+1))
        recur(sum+sign*num,-1,(n+1),n+1,string+'-'+str(n+1))

n=int(input())
for i in range(n):
    k = int(input())
    recur(0,1,1,1,"1")
    print()