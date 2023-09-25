def solution(t, p):
    answer = 0
    lt=len(t)
    lp=len(p)
    np=int(p)
    for i in range(lt-lp+1):
        part=int(t[i:i+lp])
        if part<=np:
            answer+=1
    return answer