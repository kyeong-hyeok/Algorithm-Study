from collections import deque


F, S ,G ,U ,D = map(int, input().split())
visit = [False] * (F + 1)
count = [0] * (F + 1) 

def bfs(node):
    global visit,count
    q = deque()
    q.append(node)
    visit[node] = True

    while q:
        x = q.popleft()

        if x == G:
            visit[x] = True
            return count[G]

        for i in (x+U, x-D):
             
            if 0 < i <= F and not visit[i]:
                #print("set")
                #print(i)
                visit[i] = True
                count[i] = count[x] + 1
                q.append(i)
                   
    if count[G] == 0:
        return "use the stairs"

print(bfs(S))  





