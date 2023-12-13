eyes = list(map(int,input().split()))
eyes.sort()
if eyes[0]==eyes[1] and eyes[1]==eyes[2]:
    print(10000+eyes[0]*1000)
if eyes[0]==eyes[1] and eyes[1]!=eyes[2]:
    print(1000+eyes[0]*100)
if eyes[0]!=eyes[1] and eyes[1]==eyes[2]:
    print(1000+eyes[1]*100)
if eyes[0]!=eyes[1] and eyes[1]!=eyes[2]:
    print(max(eyes)*100)