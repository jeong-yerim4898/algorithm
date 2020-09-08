def bfs(start_n):
    global cnt,visited
    q=[]
    q.append(start_n)
    visited[start_n]=1
    while q:
        starting = q.pop()
        for i in range(N+1):
            if node[starting][i]==1 and visited[i]==0:
                q.append(i)
                visited[i]=1
    return visited

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    node = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(M):
        sta,end = map(int,input().split())
        node[sta][end]=1
        node[end][sta]=1
    cnt=0
    for i in range(1,len(visited)):
        if visited[i]==0:
            bfs(i)
            cnt+=1
    print(f'#{tc} {cnt}')