n,m= int(input()),int(input())

if m != 0: 
    button= list(map(int,input().split()))

min = abs(100-n)

for numbers in range(1000001):
    numbers = str(numbers)
    for j in str(len(numbers)):
        if int(numbers[j]) in button:
            break
        elif j == len(numbers) -1:
            min = min(min,abs(int(numbers)-n)+len(numbers))

print(min)