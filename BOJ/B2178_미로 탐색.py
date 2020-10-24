def bfs(i,j):
    q=list()
    q.append((i,j))
    visited[i][j]=1
    while q:
        i,j = q.pop(0)
        for dir in dir_li:
            ni = i + dir[0]
            nj = j + dir[1]
            if -1<ni<N and -1<nj<M :
                if not visited[ni][nj] and miro[ni][nj]=='1':
                    q.append((ni,nj))
                    visited[ni][nj]= visited[i][j]+1

N,M = map(int,input().split())
miro = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dir_li = [(-1,0),(1,0),(0,-1),(0,1)] #4방 탐색
bfs(0,0) # 시작점
print(visited[N-1][M-1])
