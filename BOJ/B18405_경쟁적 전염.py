def bfs():
    while virus_li:
        num,r,c,time = virus_li.pop(0)
        if time==S:
            break
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+dir[0]
            nc = c +dir[1]
            if -1<nr<N and -1<nc<N:
                if board[nr][nc]==0:
                    board[nr][nc]=num
                    virus_li.append((num,nr,nc,time+1))


N,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
S,X,Y = map(int,input().split())
visited = [[0]*N for _ in range(N)]
virus_li=[]
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            virus_li.append((board[i][j],i,j,0))
virus_li.sort()
bfs()
if board[X-1][Y-1]!=0:
    print(board[X-1][Y-1])
else:
    print(0)
