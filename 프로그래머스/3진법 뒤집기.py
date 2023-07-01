def solution(n):
    reverse = ''
    while True :
        n, r = divmod(n, 3) 
        reverse += str(r)
        if n == 0 : break
    
    return int(reverse, 3)