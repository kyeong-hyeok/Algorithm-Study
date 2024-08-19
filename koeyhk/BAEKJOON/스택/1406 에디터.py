# N = 100,000 M = 500,000
# O(M)안에 수행을 끝내야 함 O(MN) X
# Stack 이용? 커서의 위치에 따른 유연함을 얻지 못 함

# 생각하지 못 한 부분
# 두 개의 deque를 사용하여 커서의 위치를 오른쪽 deque의 첫 부분으로 고정시킴
# 명령어에 따라 문자를 옮기고 더하며 수행

import sys
from collections import deque

input_data = sys.stdin.readline

str1 = deque(input_data().rstrip())
M = int(input_data())
str2 = deque()

for _ in range(M):
    command = input_data().rstrip().split()
    if command[0] == 'L' and str1:
        str2.appendleft(str1.pop())
    elif command[0] == 'D' and str2:
        str1.append(str2.popleft())
    elif command[0] == 'B' and str1:
        str1.pop()
    elif command[0] == 'P':
        str1.append(command[1])

print(''.join(str1+str2))