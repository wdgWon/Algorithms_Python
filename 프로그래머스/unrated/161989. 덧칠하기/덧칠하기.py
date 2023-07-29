def solution(n, m, sections):
    result = 0
    painted = 0
    for section in sections:
        if section > painted:
            painted = section + m - 1
            result += 1
    return result