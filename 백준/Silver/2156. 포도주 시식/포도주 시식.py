N=int(input())
wines=[0]*N
for i in range(N):
    wines[i]=int(input())

dp=[0]*(N+1)
dp[1]=wines[0]

def sol():
    if N<=1:
        print(dp[N])
        return

    dp[2]=dp[1]+wines[1]
    if N==2:
        print(dp[N])
        return

    if N>=3:
        for i in range(3,N+1):
            dp[i]=dp[i-3]+wines[i-2]+wines[i-1]
            dp[i]=max(dp[i],dp[i-2]+wines[i-1])
            dp[i]=max(dp[i],dp[i-1])
        print(dp[N])

sol()