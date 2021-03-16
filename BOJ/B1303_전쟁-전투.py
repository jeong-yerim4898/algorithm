from collections import deque
def bfs(r,c,color):
    global cnt
    q = deque()
    q.append((r,c))
    checked[r][c]=1
    while q:
        r,c= q.popleft()
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+dir[0]
            nc = c+dir[1]
            if -1<nr<M and -1<nc<N and not checked[nr][nc]:
                if board[nr][nc]==color:
                    checked[nr][nc]=1
                    cnt+=1
                    q.append((nr,nc))
    return cnt


N,M = map(int,input().split())
board = [list(input()) for _ in range(M)]
checked = [[0]*N for _ in range(M)]
w=0
b=0
for i in range(M):
    for j in range(N):
        if checked[i][j]==0:
            cnt=1
            bfs(i,j,board[i][j])
            if board[i][j]=='W':
                w+=cnt*cnt
            else:
                b+=cnt*cnt
print(w,b)
