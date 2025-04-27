import sys
input = sys.stdin.readline

t=int(input())

for i in range(t):
    arr=input().rstrip()
    stack=[]
    sub = []
    for i in arr:
        if i == '<':
            if stack:
                sub.append(stack.pop())
        elif i == '>':
            if sub:
                stack.append(sub.pop())
        elif i == '-':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    print("".join(stack),"".join(reversed(sub)),sep="")
