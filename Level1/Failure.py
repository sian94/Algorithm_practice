import numpy as np

def solution(N, stages):
    answer = []
    count = []
    num = []
    failure = []
    for i in range(N+1):
        
        count.append(stages.count(i+1))
    n_sum = np.sum(count)
    for i in count:
        num.append(n_sum)
        n_sum = n_sum - i
    
    for i in range(len(num)-1):
        fail = count[i]/num[i]
        failure.append(fail)
        
    f_real = failure.copy()
    failure.sort(reverse=True)

    fail_dict = {}
    
    for key, value in enumerate(f_real):
        fail_dict[key+1] = value
        
    print(fail_dict)
    
    sort_dict = sorted(fail_dict.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(sort_dict)):
        answer.append(sort_dict[i][0])

        
    return answer
