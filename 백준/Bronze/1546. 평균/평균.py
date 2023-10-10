N=int(input())
Nlist=list(map(int,input().split()))
Nlist.sort()
print(sum([i/Nlist[-1]*100 for i in Nlist])/N)