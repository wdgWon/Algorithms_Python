def solution(array, commands):
    r = []
    for c in commands:
        s = sorted(array[c[0]-1:c[1]])
        r.append(s[c[2]-1])
    return r