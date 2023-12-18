N = int(input())
f = [0]*(N+1)

def fibo(N):
    n = 0
    f[1], f[2] = 1,1
    for i in range(3,N+1):
        f[i] = f[i-1]+f[i-2]
        n += 1
    return f[N], n

met1,met2 = fibo(N)
print(f'{met1} {met2}')