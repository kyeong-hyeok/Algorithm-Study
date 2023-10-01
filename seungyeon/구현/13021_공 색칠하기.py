# 한 줄로 놓인 N개의 공
# 기계를 M번 사용했을 때 나올 수 있는 색 조합의 경우의 수 
# 애드혹 | 특정 상황에서만 정답이 되고 일반화될 수 없는 해답 = 하드코딩

n,m = map(int,input().split())
arr=[0]*n
answer = 1

def color(a,b,n):
    global answer
    for i in range(a-1,b-1):
        arr[i] = n
    answer*2

for i in range(m):
    a,b = map(int,input().split())
    color(a,b,0)
    color(a,b,1)

print(answer)

