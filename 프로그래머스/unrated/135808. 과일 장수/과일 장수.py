def solution(k, m, score):
    answer = 0
    l=len(score)
    score.sort()
    while l>=m:
        answer+=score[l-m]*m
        l=l-m
    return answer