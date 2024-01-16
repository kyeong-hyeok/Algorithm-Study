# 1) 서비스 가입자 최대 2)판매액 최대

discounts = [10, 20, 30, 40]
answer = [-1, -1]

def solution(users, emoticons):
    n, m = len(users), len(emoticons)
    arr = [0]*m
    
    def search(idx):
        global answer
        print(answer)
        if idx == m :
            plus, cost = 0, 0

            for i in range(n) :
                tmp = 0
                for j in range(m) :
                    if users[i][0] <= arr[j] : # 할인율 큰거 구매 
                        tmp += emoticons[j] * ( 100 - arr[j] ) // 100
                if tmp >= users[i][1] : # 이모티콘 플러스 서비스 가입
                    plus += 1
                else : # 그냥 구매
                    cost += tmp
            if plus > answer[0] or plus == answer[0] and cost > answer[1] : # 최대값 저장
                answer = [plus, cost]
            return
        
        for i in range(4) :
            arr[idx] = discounts[i] # 모든 할인율 탐방
            search(idx+1)
    
    search(0)
    
    return answer


solution([[40, 10000], [25, 10000]],[7000, 9000])