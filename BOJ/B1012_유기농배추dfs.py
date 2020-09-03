import sys
sys.setrecursionlimit(100000)

def dfs(y,x):
    visit[y][x]=1
    delta_li = [(1,0),(-1,0),(0,1),(0,-1)]
    for delta in delta_li:
        dy,dx = y+delta[0],x+delta[1]
        if dy<0 or dy>=N or dx<0 or dx>=M:
            continue
        elif visit[dy][dx]==0 and ground[dy][dx]==1:
            dfs(dy,dx)


T= int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    ground = [[0]*M for _ in range(N)]
    for k in range(K):
        x,y = map(int,input().split())
        ground[y][x]=1
    visit = [[0]*M for _ in range(N)]
    cnt = 0
    for y in range(N):
        for x in range(M):
            if visit[y][x]==0 and ground[y][x]==1:
                dfs(y,x)
                cnt+=1
    print(cnt)