# dict comprehension과 set의 사용법을 알아야 하는 문제
# dict의 view를 제공하는 item()
# iterable을 인자로 받아 해당 iterable을 특정 기준으로 정렬한 결과를 반환하는 sorted(): list 반환

def solution(X, Y):
    
    xDict={k:X.count(k) for k in set(X)}
    yDict={k:Y.count(k) for k in set(Y)}
    newDict={}
    
    for i in xDict:
        if i in yDict:
            newDict[i]=min(xDict[i],yDict[i])
    
    newList=[]
    for i in newDict:
        for j in range(newDict[i]):
            newList.append(i)
    
    newList.sort(reverse=True)
    answer=''.join(newList)
    
    if newList: 
        if answer[0]=='0': return '0'
        else: return answer
    else: return "-1"
    