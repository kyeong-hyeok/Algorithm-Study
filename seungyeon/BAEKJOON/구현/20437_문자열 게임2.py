import sys
input=sys.stdin.readline

n=int(input())

for i in range(n):
    word=str(input().rstrip())
    k=int(input())
    num=[[] for _ in range(27)]
    answer=[]

    for i in range(len(word)):
        alphabet = ord(word[i])-ord('a')
        num[alphabet].append(i)

        if len(num[alphabet]) >= k:
            answer.append(word[num[alphabet][-k]:num[alphabet][-1]+1])

    if len(answer) == 0:
        print(-1)
    else:
        answer.sort(key=lambda x:len(x))
        print(len(answer[0]),len(answer[-1]))

