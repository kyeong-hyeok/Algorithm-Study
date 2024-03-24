
import sys
input=sys.stdin.readline

def reverse(bulbs,count):
    for i in range(1,n-1):
        if bulbs[i-1] != after[i-1]: # 다르면 
            count += 1
            for j in range(i-1,i+2): # 버튼 누르기 
                bulbs[j] = not bulbs[j]

    if bulbs[n-1] != after[n-1]:
        count += 1
        bulbs[n-2] = not bulbs[n-2]
        bulbs[n-1] = not bulbs[n-1]
    
    if bulbs == after:
        return count 
    else:
        return -1
    
n = int(input())
before = list(map(bool,map(int,input().rstrip())))
after = list(map(bool,map(int,input().rstrip())))

# 첫번째를 눌렀을 때 
on = before.copy()

on[0] = not on[0]
on[1] = not on[1]

if before == after:
    print(0)
else:
    count = reverse(before,0)
    if count != -1:
        print(count)
    else:
        count = reverse(on,1)
        print(count if count else -1)