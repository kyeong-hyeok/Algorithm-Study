def prime(a):
    if a <= 1:
        return 0
    ra = int(a**(1/2)) + 1
    for i in range(2, ra):
        if a % i == 0:
            return 0
    return 1


def solution(n, k):
    kn = ''
    result = 0
    while n > 0:
        n, m = divmod(n, k)
        kn += str(m)
    kn = kn[::-1]
    for i in kn.split('0'):
        if i == '':
            continue
        if prime(int(i)) == 1:
            result += 1
    return result