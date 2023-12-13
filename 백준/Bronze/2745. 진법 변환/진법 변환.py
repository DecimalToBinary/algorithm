# 주어진 B진법 문자열을 마지막 자리부터 계산해나가며 답을 완성하기 위해 ''.join(reversed(N)) 사용
N,B = map(str, input().split())
B = int(B)
N = ''.join(reversed(N))
ans = 0
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lN = len(N)

for i in range(len(N)):
    ans += characters.index(N[i])*(B**i)

print(ans)