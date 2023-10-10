from collections import deque

def solution(pep,lim):
    answer=0
    pep.sort()
    deque1=deque(pep)
    
    while deque1:
        if len(deque1)==1:
            deque1.pop()
        else:
            if deque1[0]+deque1[-1]>lim:
                deque1.pop()
            else:
                deque1.pop()
                deque1.popleft()
        answer+=1
    return answer