import sys

input_data = sys.stdin.readline

N = int(input_data())
pattern = input_data().split("*")
left, right = len(pattern[0]), len(pattern[1])
for i in range(N):
    file = input_data()
    p = 'NE'
    if left + right <= len(file) and pattern[0] == file[:left] and pattern[1] == file[-right:]:     # 패턴의 길이보다 문자열이 길어야함!!
        p = 'DA'
    print(p)
