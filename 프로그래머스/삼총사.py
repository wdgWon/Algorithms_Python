from itertools import combinations

def solution(number):
    combi = list(combinations(number, 3))
    result = list(filter(lambda a: a[0]+a[1]+a[2] == 0, combi))
    return len(result)