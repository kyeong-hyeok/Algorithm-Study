# n = 1,000,000 -> O(N)

import sys

input_data = sys.stdin.readline

n = int(input_data())
d = dict()

for i in range(n):
    name, s = input_data().split()
    if s == 'enter':
        d[name] = 1
    else:
        del d[name]

print('\n'.join(sorted(d.keys(), reverse=True)))