from collections import Counter

def solution(topping):
    answer=0
    brotherCount=Counter(topping)
    chul=set([])
    for i in topping:
        if i not in chul:
            chul.add(i)
        brotherCount[i]-=1
        if brotherCount[i]==0:
            del brotherCount[i]
        if len(chul)==len(brotherCount):
            answer+=1
    return answer