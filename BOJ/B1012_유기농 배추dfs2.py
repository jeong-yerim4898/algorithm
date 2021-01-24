import sys
sys.setrecursionlimit(100000)

def dfs(r,c):
    mapping[r][c]=0
    for dir in dir_li:
        nr = r+dir[0]
        nc = c+dir[1]
        if -1<nr<N and -1<nc<M and mapping[nr][nc]==1:
            dfs(nr,nc)
T = int(input())
for tc in range(1,T+1):
    M,N,K=map(int,input().split()) #가로,세로,개수
    mapping=[[0]*M for _ in range(N)]
    dir_li = [(-1,0),(1,0),(0,-1),(0,1)]
    cnt=0
    for _ in range(K):
        s,e = map(int,input().split())
        mapping[e][s]=1
    for r in range(N):
        for c in range(M):
            if mapping[r][c]==1:
                dfs(r,c)
                cnt+=1
    print(cnt)