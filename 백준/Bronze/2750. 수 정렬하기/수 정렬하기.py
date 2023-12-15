N = int(input())
lis = [0]*N
for i in range(N):
    lis[i] = int(input())

lis.sort()
for i in range(N):
    print(lis[i])