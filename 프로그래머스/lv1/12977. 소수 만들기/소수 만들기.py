def solution(nums):
    import math

    def is_prime_num(n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    import itertools
    arr = itertools.combinations(nums, 3)
    cnt = 0
    for numbers in arr:
        if(is_prime_num(sum(numbers))):
            cnt += 1
    return cnt