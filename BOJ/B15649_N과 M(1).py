def powerset(idx):
    if idx==M:
        print(*ans)
        return
    for i in range(N):
        if visited[i]!=0:
            continue
        ans[idx]=i+1
        visited[i]=1
        powerset(idx+1)
        visited[i]=0

N,M=map(int,input().split())
visited=[0]*(N)
ans=[0]*M
powerset(0)