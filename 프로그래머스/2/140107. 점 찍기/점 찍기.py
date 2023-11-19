from math import sqrt

def solution(k, d):
    answer = 0
    ddivk=int(d/k)
    for x in range(int(d/k)+1):
        while sqrt((x*k)**2+(ddivk*k)**2)>d:
            ddivk-=1
        answer+=(ddivk+1)
    return answer