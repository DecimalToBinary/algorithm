N = input()
nN = int(N)

for i in range(1, nN+1):
    s = sum(map(int,str(i)))
    if nN == s+i:
        print(i)
        break
    if i == nN:
        print(0)