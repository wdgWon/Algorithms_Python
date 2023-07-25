def solution(n):
    # n을 포함시키기 위함
    n += 1
    # [False(0), False(1), True(2), True(3), True(4) ... True(n)]
    sieve = [False, False] + [True] * (n)
    end = int(n ** 0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i + i, n, i):
                sieve[j] = False
                
    return len([i for i in range(n) if sieve[i] == True])