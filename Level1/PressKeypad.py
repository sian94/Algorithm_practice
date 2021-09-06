import numpy as np

def solution(numbers, hand):
    
    answer = ''
    keypad = np.array([['*','0','#'],['7','8','9'],['4','5','6'],['1','2','3']])
    right_pos = (0,0)
    left_pos = (0,2)
    
    for num in numbers:
        if num in [1,4,7]:
            x, y = np.where(keypad == str(num))
            left_pos = (int(x), int(y))
            answer += 'L'
        elif num in [3,6,9]:
            x,y = np.where(keypad == str(num))
            right_pos = (int(x), int(y))
            answer +='R'
        else:
            x,y = np.where(keypad == str(num))
            num_pos = np.concatenate((x,y))
            
            left_dist = np.sum(np.abs(num_pos - np.array(left_pos)))
            right_dist = np.sum(np.abs(num_pos - np.array(right_pos)))
            
            if left_dist < right_dist:
                answer +='L'
                left_pos = tuple(num_pos)
            elif right_dist < left_dist:
                answer += 'R'
                right_pos = tuple(num_pos)
            elif right_dist == left_dist:
                if hand == 'left':
                    answer += 'L'
                    left_pos = tuple(num_pos)
                elif hand == 'right':
                    answer += 'R'
                    right_pos = tuple(num_pos)
            
    return answer
