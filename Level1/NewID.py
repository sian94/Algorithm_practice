def solution(new_id):
    answer = ''
    can_use = list('abcdefghijklmnopqrstuvwxyz0123456789-_.')

    new_id = new_id.lower()
    list_new = list(new_id)
    
    for i in list_new[:]:
        
        if i not in can_use:
            list_new.remove(i)
            
    list3 =[]
    
    for i in range(len(list_new)):
        if(list_new[i] == '.' and list_new[i-1]=='.'):
            continue
        else:
            list3.append(list_new[i])
    
    if(len(list3)!=0):
        if(list3[0] == '.'):
            list3.pop(0)
        if(list3[-1] == '.'):
            list3.pop(-1)
    
    if(len(list3) == 0):
        list3 = ['a']
    elif(len(list3) >= 16):
        list3 = list3[:15]
        if(list3[-1] =='.'):
            list3.pop(-1)
    
    if(len(list3) <=2):
        last = list3[-1]
        
        for i in range(3-len(list3)):
            list3.append(last)
    
    for ans in list3:
        answer += ans
    
    return answer
