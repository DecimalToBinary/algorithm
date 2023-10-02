def solution(num_list):
    oddSum=0
    evenSum=0
    for i in list(enumerate(num_list,start=1)):
        if i[0]%2==1:
            oddSum+=i[1]
        else:
            evenSum+=i[1]
    return oddSum if oddSum>=evenSum else evenSum