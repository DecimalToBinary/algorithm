N = int(input())
pointList = []
for i in range(N):
    pointList.append(tuple(map(int,input().split())))
    
pointList = sorted(pointList, key=lambda x:(x[0],x[1]))
for i in range(N):
    print(f'{pointList[i][0]} {pointList[i][1]}')