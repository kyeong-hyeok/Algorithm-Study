import sys
input=sys.stdin.readline

n,m=map(int,input().split())

arr=[]
house=[]
chicken=[]
for i in range(n):
    arr_n=list(map(int,input().split()))
    for j in range(n):
        if arr_n[j] == 1:
            house.append((i,j))
        elif arr_n[j] == 2:
            chicken.append((i,j))

visited=[False]*len(chicken)

min_ans = 99999999

def dfs(index,count):

    global min_ans

    # 거리가 최단거리보다 크다면 유망하지 않음? -> 다 순회해야 최단거리 찾을 수 있음
    # 각 집과 치킨집 사이 거리 메모제이션?


    if count == m:
        ans = 0

        for i in house:
            distance=999999
            
            for j in range(len(visited)):
                if visited[j]:
                    check=abs(i[0]-chicken[j][0])+abs(i[1]-chicken[j][1])
                        # a번째 매장과 집들간의 최단거리 갱신
                    distance=min(distance,check)

            ans += distance
        min_ans=min(ans,min_ans)

        return



    # permutation -> 백트래킹
    # len(chicken) 중 a번째 선택
    for i in range(index,len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,count+1)
            visited[i]=False

dfs(0,0)
print(min_ans)

