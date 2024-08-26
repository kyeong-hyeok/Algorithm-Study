import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
well_cost = [int(input()) for _ in range(N)]
road_list = list()
for i in range(N) :
  road_cost = list(map(int, input().split()))
  for j in range(i+1, N) :
    road_list.append((road_cost[j], i, j))

road_list.sort()
parent = [(i, well_cost[i]) for i in range(N)]

def find(a) :
  if a == parent[a][0] :
    return parent[a]
  parent[a] = find(parent[a][0])
  return parent[a]

def union(a, b) :
  pa, pa_cost = find(a)
  pb, pb_cost = find(b)
  if pa_cost < pb_cost :
    parent[pb] = (pa, pa_cost)
  else :
    parent[pa] = (pb, pb_cost)

answer, cnt = 0, N-1
for cost, a, b in road_list :
  if not cnt :
    break
  pa, pa_cost = find(a)
  pb, pb_cost = find(b)
  if pa != pb and max(pa_cost, pb_cost) >= cost :
    cnt -= 1
    union(a, b)
    answer += cost

tree_set = set()
for i in range(N) :
  pi, pcost = find(i)
  if pi not in tree_set :
    tree_set.add(pi)
    answer += pcost
    
print(answer)


# import sys
# input=sys.stdin.readline
# MAX=float('inf')

# n = int(input().rstrip())
# well_cost = [int(input())  for _ in range(n)]
# road_list=list()

# for i in range(n):
#     road_cost = list(map(int,input().split()))
#     for j in range(i+1,n):
#         road_list.append((road_list[j], i, j))
# road_list.sort()
# parent=[ (i,well_cost[i]) for i in range(n)]

# def get_parent(x):
#     if parent[x] ==parent[x][0] :
#         return parent[x]
#     parent[x] = get_parent(parent[x][0])
#     return parent[x]

# def is_same_parent(a,b):
#     return get_parent(a) == get_parent(b)


# def union_parent(a,b):
#     pa, pa_cost = get_parent(a)
#     pb,pb_pb_cost = get_parent(b)

#     if a < b:
#         parent[pb] = (pa,pa_cost)
#     else:
#         parent[pa] = (pb,pb_pb_cost)


# answer,cnt = 0,n

# for cost,a,b in road_list:
#     if not cnt: 
#         break

#     pa,pa_cost = get_parent(a)
#     pb ,pb_cost= get_parent(b)

#     if not is_same_parent(pa,pb) and max(pa_cost,pb_cost) >= cost:
#         cnt -=1
#         union_parent(a,b)
#         answer += cost

# tree_set=set()

# for i in range(n):
#     pi,pcost=get_parent(i)
#     if pi not in tree_set:
#         tree_set.add(pi)
#         answer += pcost

# print(answer)