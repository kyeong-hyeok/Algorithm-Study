import sys
input=sys.stdin.readline

n,r,c=map(int,input().split(" "))

# r행 c열을 몇번째로 방문하는지 출력
# r행 c열이 전체중에 몇번째인지 .. 
# 4칸중에 몇번째인지만 알면됨
# r행 / 2의 3승
# c열 / 2의 3승


def sol(n,r,c):
    if n==0:
        return 0
    return 2+(r%2)+(c%2) + 4*sol(n-1,int(r/2),int(c/2))