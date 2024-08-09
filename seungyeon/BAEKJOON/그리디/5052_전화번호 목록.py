import sys
input=sys.stdin.readline

t = int(input())
for i in range(t):
    result = False

    n = int(input())

    phone = []
    for i in range(n):
        phone.append(input().strip())

    phone.sort()

    for i in range(n-1):
        if len(phone[i]) < len(phone[i+1]):
            if phone[i] == phone[i+1][:len(phone[i])]:
                result = True
                break
    if result:
        print("NO")
    else:
        print("YES")