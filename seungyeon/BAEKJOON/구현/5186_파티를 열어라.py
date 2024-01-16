k = int(input())
n,c,l = map(int,input().split())
arr=dict()
car=[]
answer=0
for i in range(n):
    a,b = input().split()
    try:
        arr[(a,b)] += 1
    except:
        arr[(a,b)] = 1
for j in range(c):
    a,b = input().split()
    car.append ((a,b))
    
for a,b in sorted(list(arr.keys()),key=lambda x: x[0]):
    for x in car:        
        p,q = map(int,list(x))
        if p == int(a) and q != 0:
            q -=1
            answer +=1
        
print(answer)
