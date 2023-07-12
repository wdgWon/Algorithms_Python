def solution(numbers):
    from itertools import combinations
    return sorted(list(set(map(lambda x: sum(x), combinations(numbers, 2)))))