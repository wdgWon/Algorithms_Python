import math

def solution(left, right):
    result = 0
    
    def measureCount(n):
        measures = set()
        for i in range(1, int(math.sqrt(n))+1):
            if(n % i == 0):
                measures.update([i, n/i])
        return len(measures)

    for number in range(left, right+1):
        if(measureCount(number) % 2):
            result -= number
        else:
            result += number
    
    return result