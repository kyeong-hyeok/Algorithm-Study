def fib(n):
    zeros=[1,0,1]
    ones=[0,1,1]
    if n >= 3:
        for i in range(2,n):
            zeros.append(zeros[i-1] + zeros[i])
            ones.append(ones[i-1] + ones[i])
    print(zeros[n], ones[n])
 
t = int(input())
for _ in range(t):
    n = int(input())
    fib(n)