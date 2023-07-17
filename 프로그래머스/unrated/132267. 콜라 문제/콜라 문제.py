def solution(a, b, n):
    cnt = 0
    while(True):
        if(n < a):
            break
        q = n // a
        m = q * b
        n = n % a + m
        cnt += m
    return cnt