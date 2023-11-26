TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    S = input()
    if N % 2 != 0:
        print(f"#{i} No")
        continue
    S = list(S)
    if S[:N//2] == S[N//2:N]:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")