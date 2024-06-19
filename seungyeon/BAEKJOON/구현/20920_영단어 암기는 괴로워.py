import sys
from collections import defaultdict
input=sys.stdin.readline

n,m=map(int,input().rstrip().split())
words=defaultdict(int)
for i in range(n):
    word=input().rstrip()
    
    if len(word) >= m:
        words[word] += 1

words = sorted(words.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for i in words:
    print(i[0])

