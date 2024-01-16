def solution(n, k):
    answer = 0
    str = toDegree(n,k)
    for s in str.split('0'):
        if s == "": continue
        if isPrime(int(s)):
            print(s)
            answer+=1
    return answer

def toDegree(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def isPrime(x):
    if x == 1: return False
    for i in range(2, x):
    	if x % i == 0:
            return False
    return True

print(solution(437674,3))
