#bin()함수와 count()함수를 알면 간단히 풀 수 있는 문제였다...
#dfs 알고리즘 문제 풀듯 풀어야 한다고 생각하고 푸는 방식을 고민하는데 시간을 많이 썼는데, 그 방식으로 결과를 내지 못했다.

def solution(n):
    answer=0
    ncount=bin(n)[2:].count('1')
    
    for i in range(n+1,1000000):
        icount=bin(i)[2:].count('1')
        if icount==ncount:
            answer=i
            break
    
    return answer