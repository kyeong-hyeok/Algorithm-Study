# 2의 15승 = 32768 * 32768 = 
# 을 모두 탐색하면 -> 시간초과?
# r행 c열을 방문하려면 분할 탐색으로 접근 ..?

# 1,2,3,4 중에 그 위치만 알고 나머지는 4 더하면 될듯
# 1,2,3,4 중에 위치는 어떻게 알지?

# 위치 넣으면 계산하기

# (0,0)(1,0)(0,1)(1,1)

def dc(x,y,n):
    global cnt
    if x>r or x+n <= r or y>c or y+n <= c:
        cnt += n**2
        return 
    
    if n > 2:
        n//=2
        dc(x,y,n)
        dc(x,y+n,n)
        dc(x+n,y,n)
        dc(x+n,y+n,n)
    else: # 최소 단위
        if x==r and y==c: # (0,0)
            print(cnt)
        elif x==r and y+1==c: # (1,0)
            print(cnt+1)
        elif x+1==r and y==c: # (0,1)
            print(cnt+2)
        else: # (1,1)
            print(cnt+3)
        return 
n,r,c = map(int,input().split())
cnt = 0
dc(0,0,n**2)