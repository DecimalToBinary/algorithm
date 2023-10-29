kg=int(input())
answer=0

while (kg>=0 and kg<3) is not True:
    if kg%5!=0: 
        kg-=3
    else:
        kg-=5
    answer+=1

if kg==0: print(answer)
else: print(-1)