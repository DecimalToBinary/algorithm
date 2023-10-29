N,M=map(int,input().split())
NList=list(map(int,input().split()))
sumList=[]

for i in range(len(NList)):
    for j in range(i+1,len(NList)):
        for k in range(j+1,len(NList)):
            NS=NList[i]+NList[j]+NList[k]
            if NS<=M:
                sumList.append(NS)

print(max(sumList))