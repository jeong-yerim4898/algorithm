def back(idx,next):
    if idx==M:
        print(*ans)
        return
    for i in range(next,N):
        if visited[i]==0:
            ans[idx]=i+1
            visited[i]=1
            back(idx+1,i+1)
            visited[i]=0
N,M = map(int,input().split())
ans = [0]*M
visited=[0]*N
back(0,0)