def solution(food):
    s = ''
    c = 0
    for f in food:
        n = f // 2
        if n != 0:
            s = s + (str(c) * n)
        c += 1
    return s + "0" + s[::-1]