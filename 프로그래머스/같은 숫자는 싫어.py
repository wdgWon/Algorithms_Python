def solution(s):
    a = [s[0]]
    for i in s:
        if a[-1] != i: a.append(i)
    return a