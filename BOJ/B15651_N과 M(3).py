def nandm(idx):
    if idx==M:
        print(*ans)
        return
    for i in range(0,N):
        ans[idx] = i + 1
        nandm(idx + 1)

N,M =map(int,input().split())
ans=[0]*M
nandm(0)