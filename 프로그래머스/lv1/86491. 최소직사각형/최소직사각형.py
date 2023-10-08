def solution(sizes):
    sizes.sort(reverse=True)
    tmp=sizes[0]
    garo=tmp[0]
    sero=tmp[1]
    
    for i in sizes[1:]:
        i.sort(reverse=True)
        if i[0]>tmp[0]:
            garo=i[0]
            tmp[0]=i[0]
        if i[1]>tmp[1]:
            sero=i[1]
            tmp[1]=i[1]
    
    return garo*sero