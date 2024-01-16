n = int(input())
arr = [list(map(int,(input()))) for _ in range(n)]
answer = []

#(0~n/2,0,n/2) | (n/2-n,0-n/2)
# (0-n/2,n/2-n) |( n/2 - n, n/2 - n)

def divide(x,y,n):
    global answer
    color = arr[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                answer.append("(")
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                answer.append(")")
                return

    answer.append(color)

divide(0,0,n)
print("".join(map(str,answer)))