N,K = map(int,input().split())
coin_li = list(int(input()) for _ in range(N))
ans = 0
for i in range(N-1,-1,-1):
    if K//coin_li[i]!=0:
        ans+=K//coin_li[i]
        K = K%coin_li[i]
if K!=0:
    print(0)
else:
    print(ans)