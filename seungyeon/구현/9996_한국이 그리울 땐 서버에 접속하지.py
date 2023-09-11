n = int(input())
pattern = input()

arr = list(pattern.split("*"))
for i in range(n):
    str = input()
    if( (str.startswith(arr[0]) and str.endswith(arr[1]))):
        print("DA")
    else:
        print("NE")