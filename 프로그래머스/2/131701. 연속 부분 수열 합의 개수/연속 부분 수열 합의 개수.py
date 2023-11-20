'''from math import ceil

def solution(elements):
    answer = []
    le = len(elements)
    i = 1  # 연속 부분 수열의 길이
    s = 0  # 부분합 임시 저장
    elementsSum = sum(elements)
    
    while i<=ceil((le-1)/2):
        for x in range(le): # 연속 부분 수열의 시작 인덱스 x
            for y in range(i):  # 시작 인덱스 x에서 i-1번만큼 이동하며 해당 인덱스의 수 sum에 더함. 그 인덱스 가리키기 위한 y
                s += elements[(x+y) % le]
            answer.append(s)
            answer.append(elementsSum-s)
            s = 0
        i += 1
        
    return len(set(answer))+1
    '''

def solution(elements):
    sums, n = [], len(elements)
    elements += elements[:-1]
    for i, a in enumerate(elements):
        SUM = a
        sums.append(SUM)
        for b in elements[i + 1:i + n]:
            SUM += b
            sums.append(SUM)

    return len(list(set(sums)))
