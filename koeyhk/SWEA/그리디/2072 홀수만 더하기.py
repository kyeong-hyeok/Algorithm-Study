T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    total = 0
    for n in numbers:
        if n % 2 != 0:
            total += n
    print(f"#{i} {total}")