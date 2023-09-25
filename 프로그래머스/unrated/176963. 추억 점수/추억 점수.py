def solution(name, yearning, photo):
    answer = []
    d=dict(zip(name,yearning))
    for p in photo:
        s=0
        for people in p:
            if people in d:
                s+=d[people]
        answer.append(s)
    return answer