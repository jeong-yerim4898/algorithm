def nandm(idx,next):
    if idx==M:
        print(*ans)
        return
    for i in range(next,N):
        ans[idx]=i+1
        nandm(idx++1,i)
N,M =map(int,input().split())
ans=[0]*M
nandm(0,0)