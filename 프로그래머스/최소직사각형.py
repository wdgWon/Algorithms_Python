def solution(sizes):
    m, n = 0, 0
    for col, row in sizes:
        if col < row:
            col, row = row, col
        m = max(m, col)
        n = max(n, row)
    
    return m * n