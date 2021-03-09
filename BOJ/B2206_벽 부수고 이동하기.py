from collections import deque

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0]=1
    while q:
        x,y,z = q.popleft()
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dir[0]
            ny = y + dir[1]
            if -1<nx<N and -1<ny<M:
                if mapping[nx][ny]==0 and visited[nx][ny][z]==-1: # 범위안에 있고 방문하지 않았다면
                    visited[nx][ny][z]= visited[x][y][z]+1
                    q.append([nx,ny,z])
                elif z==0 and mapping[nx][ny]==1 and visited[nx][ny][z+1]==-1:# 방문안했고 벽이 있다고 벽을 부수지 않았다면
                    visited[nx][ny][z+1] = visited[x][y][z]+1
                    q.append([nx,ny,z+1])
N,M = map(int,input().split())
mapping = [list(map(int,input())) for _ in range(N)]
visited =  [[[-1] * 2 for i in range(M)] for i in range(N)]
bfs()

ans1, ans2 = visited[N-1][M-1][0], visited[N-1][M-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))