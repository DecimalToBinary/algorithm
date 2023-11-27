def solution(order):
    answer,cur=0,0
    stack=[]
    
    for i in range(1,len(order)+1):
        stack.append(i)
        while stack and stack[-1]==order[cur]:
            stack.pop()
            answer+=1
            cur+=1
    return answer