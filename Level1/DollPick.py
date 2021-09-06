import numpy as np

def solution(board, moves):
    answer = 0
    stack=[]
    board = np.array(board)
    
    for m in moves:
        curr_col = board[:,m-1]
        for i in range(len(curr_col)):
            
            if curr_col[-1] == 0:
                curr = None
                break
            
            if curr_col[i] != 0:
                curr = curr_col[i]
                curr_col[i] = 0
                board[:,m-1] = curr_col
                break

        if(len(stack) ==0):
            stack.append(curr)
        else:
            if (curr == None):
                continue
            if(curr == stack[-1]):
                stack.pop()
                answer +=2
            else:
                stack.append(curr)

    return answer
