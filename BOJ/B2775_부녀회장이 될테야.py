T= int(input())
for tc in range(1,T+1):
    k = int(input())
    n = int(input())
    dp = [[0]*15 for _ in range(15)]
    for j in range(1,15):
        dp[0][j]=j
    for i in range(1,15):
        for j in range(1,15):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    print(dp[k][n])