def solution(numLog):
    result=''
    dict={-10:'a',-1:'s',1:'w',10:'d'}
    for i in range(len(numLog)-1):
        result+=dict[numLog[i+1]-numLog[i]]
    
    return result    