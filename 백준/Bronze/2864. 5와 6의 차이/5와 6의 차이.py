A,B=map(int,input().split())
A=str(A)
B=str(B)
maxHap,minHap=0,0

for i in A:
    if i=='5': A=A.replace('5','6')
for i in B:
    if i=='5': B=B.replace('5','6')

maxHap=int(A)+int(B)

for i in A:
    if i=='6': A=A.replace('6','5')
for i in B:
    if i=='6': B=B.replace('6','5')
        
minHap=int(A)+int(B)

print(f'{minHap} {maxHap}')