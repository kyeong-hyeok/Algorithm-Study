import sys
input=sys.stdin.readline

n = int(input())
arr=list(map(int,input().split()))

arr.sort()
answer = sys.maxsize

for i in range(n):
    for j in range(i+3,n):
        l,r=i+1,j-1

        while l < r:
            tmp = (arr[i] + arr[j]) - (arr[l]+arr[r])

            if abs(answer) > abs(tmp):
                answer = abs(tmp)

            elif tmp == 0:
                answer = 0
                print(answer)
                exit() 
            
            if tmp < 0: # 음수라면, 그 다음에 더 좋은 값이 나올 수 없음 right -= 1
                r -= 1
            else: # 양수라면 left 를 줄여도 됨 
                l += 1

        
            #  3-2. 두 번째 눈사람의 키가 첫번째 눈사람보다 작다면 left를 1증가시켜서
            #         두 번째 눈사람의 키를 증가시킨다. (첫번째 눈사람은 고정이므로 크기를 변경하면 안된다.)
        
            #  3-3. 두 번째 눈사람의 키가 첫번째 눈사람보다 크다면 right를 1 감소시켜서
            #          두 번째 눈사람의 키를 감소시킨다.
print(answer)