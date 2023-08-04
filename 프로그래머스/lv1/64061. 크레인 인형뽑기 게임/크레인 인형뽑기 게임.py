def solution(board, moves):
    board_stack = [[] for _ in range(len(board))]
    stack = []
    result = 0
    
    for i, row in enumerate(board[::-1]):
        for j, col in enumerate(row):
            if col != 0:
                board_stack[j].append(col)
                
    for move in moves:
        if len(board_stack[move-1]) < 1: 
            continue
        pick = board_stack[move-1].pop()
        if len(stack) > 0 and pick == stack[-1]:
            stack.pop()
            result += 2
        else:
            stack.append(pick)
        
    return result
        