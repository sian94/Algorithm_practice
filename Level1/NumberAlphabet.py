def solution(s):
    answer = ''
    num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    num_list = ['1','2','3','4','5','6','7','8','9','0']
    curr = ''
    
    for i in str(s):
        if( i in num_list):
            answer += i
            curr=''
        else:
            curr +=i
            
            if( curr in num_dict.keys()):
                answer += str(num_dict[curr])
                curr=''
        
        print(curr)
    
    return int(answer)
