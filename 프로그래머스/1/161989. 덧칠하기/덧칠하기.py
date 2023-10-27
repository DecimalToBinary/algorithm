from collections import deque

def solution(n, m, section):
    answer=1
    startLoc=section[0]
    
    while section:
        for i in section:
            if i>=startLoc and i<=startLoc+m-1:
                section=section[1:]
            else:
                answer+=1
                startLoc=section[0]
                break
        
    return answer