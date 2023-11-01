T = int(input())

for i in range(1, T+1):
    a, b, c = map(int, input().split())
    x = b - a
    y = c - b
    print(f"#{i} {abs(x-y)/2}")

