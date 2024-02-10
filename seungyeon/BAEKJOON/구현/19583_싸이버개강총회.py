import sys
from collections import deque
input=sys.stdin.readline

start,end,stream=input().split()
start=int(start[:2] + start[3:])
end=int(end[:2] + end[3:])
stream=int(stream[:2] + stream[3:])

members = set()
answer = 0
while True:
    try:
        time,name=input().split()
        time=int(time[:2] + time[3:])
        if time <= start: # 출석
            members.add(name)
        elif end <= time <= stream and name in members:
            members.remove(name)
            answer += 1
    except:
        break
print(answer)