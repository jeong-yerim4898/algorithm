#최소 bfs
from collections import deque
def bfs(r,c):
    q=deque()
    q.append((r,c))
    visited[r][c]=1
    while q:
        r,c = q.popleft()
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+dir[0]
            nc = c+dir[1]
            if -1 < nr < N and -1 < nc < M:
                if not visited[nr][nc] and mapping[nr][nc]=='1':
                    q.append((nr,nc))
                    visited[nr][nc]=visited[r][c]+1


N,M = map(int,input().split())
mapping = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
bfs(0,0)
print(visited[N-1][M-1])