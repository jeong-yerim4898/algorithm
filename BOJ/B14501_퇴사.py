# DP를 활용한 문제

N = int(input()) # 요일수
T,P = [0]*(N+1),[0]*(N+1)
for i in range(1,N+1):
    T[i],P[i] = map(int,input().split())
dp=[0]*25
for i in range(1,N+1):
    if dp[i] > dp[i+1]:
        dp[i+1] =dp [i]
    if dp[i+T[i]]<dp[i]+P[i]:
        dp[i+T[i]]=dp[i]+P[i]
print(dp[N+1])