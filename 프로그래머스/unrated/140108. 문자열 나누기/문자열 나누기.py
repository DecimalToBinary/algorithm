def solution(s):
    answer = 0
    b1=""
    b2=""
    for ss in s:
        if b1=="":
            b1+=ss
        else:
            if b1[0]!=ss:
                b2+=ss
            else:
                b1+=ss
        
        if len(b1)==len(b2):
            answer+=1
            b1=""
            b2=""
    
    if len(b1)>0:
        answer+=1
    return answer