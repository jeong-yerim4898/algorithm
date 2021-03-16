def bfs(r,c,cnt):
    q=[(r,c,cnt)]
    dir_li = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
    while q:
        r,c,cnt = q.pop(0)
        for dir in dir_li:
            nr=r+dir[0]
            nc =c+dir[1]
            if -1<nr<N and -1<nc<N and not checked[nr][nc]:
                if mapping[nr][nc]==1:
                    return cnt
                else:
                    checked[nr][nc]=1
                    q.append((nr,nc,cnt+1))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping=[[0]*N for _ in range(N)]
    checked=[[0]*N for _ in range(N)]
    sr,sc = map(int,input().split())
    er,ec = map(int,input().split())
    mapping[er][ec]=1
    if sr==er and sc==ec:
        print(0)
    else:
        print(bfs(sr,sc,1))
