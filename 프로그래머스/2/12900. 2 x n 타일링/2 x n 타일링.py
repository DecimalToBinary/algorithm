nlist=[0]*60001
def solution(n):
    nlist[1]=1
    nlist[2]=2
    for i in range(3,n+1):
        nlist[i]=(nlist[i-2]+nlist[i-1])%1000000007
    
    return nlist[n]