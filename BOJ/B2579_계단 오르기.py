N = int(input())
stairs=[0]*301
dp = [0]*301
for i in range(N):
    stairs[i]=int(input())
dp[0]=stairs[0]
dp[1]=stairs[0]+stairs[1]
dp[2]=max(stairs[0]+stairs[2],stairs[1]+stairs[2])
for s in range(3,N):
    dp[s]=max(dp[s-2]+stairs[s],dp[s-3]+stairs[s-1]+stairs[s])
print(dp[N-1])
