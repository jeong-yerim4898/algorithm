def bfs(queue):
    global cnt
    q = list()

    while len(queue):
        for pos in queue:
            x = pos[0]
            y = pos[1]
            z = pos[2]
            for delta in  delta_li:
                nx = x + delta[0]
                ny = y + delta[1]
                nz = z + delta[2]
                if -1 < nx < H and -1 < ny < N and -1 < nz < M and boxes[nx][ny][nz] == 0:
                    boxes[nx][ny][nz]=1
                    q.append((nx,ny,nz))
        cnt+=1
        queue=q
        q=list()

M,N,H = map(int,input().split())
zero_cnt = 0
boxes = list()
cnt=-1
boxes=[[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
delta_li = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
queue= list()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 1:
                queue.append((i,j,k))
bfs(queue)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if boxes[i][j][k] == 0:
                cnt= -1

print(cnt)

