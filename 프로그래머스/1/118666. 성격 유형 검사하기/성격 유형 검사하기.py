def solution(survey, choices):
    answer = ''
    dp1={"R":0,"C":0,"J":0,"A":0}
    dp2=["T","F","M","N"]
    index=0
    
    for s in survey:
        ls=list(s)
        lss=sorted(ls)
        
        if ls[0]==lss[0]:
            if choices[index]==1:
                dp1[lss[0]]+=3
            elif choices[index]==2:
                dp1[lss[0]]+=2
            elif choices[index]==3:
                dp1[lss[0]]+=1
            elif choices[index]==4:
                dp1[lss[0]]+=0
            elif choices[index]==5:
                dp1[lss[0]]-=1
            elif choices[index]==6:
                dp1[lss[0]]-=2
            else:
                dp1[lss[0]]-=3
            
        else:
            if choices[index]==1:
                dp1[lss[0]]-=3
            elif choices[index]==2:
                dp1[lss[0]]-=2
            elif choices[index]==3:
                dp1[lss[0]]-=1
            elif choices[index]==4:
                dp1[lss[0]]+=0
            elif choices[index]==5:
                dp1[lss[0]]+=1
            elif choices[index]==6:
                dp1[lss[0]]+=2
            else:
                dp1[lss[0]]+=3
        
        index+=1
        
    i=0    
        
    for shape in dp1:
        if dp1[shape]>=0: answer+=list(dp1.keys())[i]
        else: answer+=dp2[i]
        i+=1
        
    return answer