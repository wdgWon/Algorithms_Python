def solution(strings, n):
    return sorted(strings, key=lambda s: s[n] + s[0:n] + s[n+1:])