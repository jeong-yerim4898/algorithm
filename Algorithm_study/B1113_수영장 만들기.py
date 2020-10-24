# bfs
def bfs(i,j,h):
    q=list()
    pos_li = [(i,j)]
    q.append((i,j))
    visited[i][j]=True
    status = False
    while q:
        x,y = q.pop(0)
        for dir in dir_li:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny]:
                    if ground[nx][ny]<h:
                        visited[nx][ny]=True
                        q.append((nx,ny))
                        pos_li.append((nx,ny))
            else: # 불가능 한 상태
                status = True
    if status:
        return 0
    else:
        water = 0
        for pos in pos_li:
            ground[pos[0]][pos[1]]+=1 # 물 높이 1 높여주기
            water +=1 # 총 물의 양을 구하기 위한 변수
        return water

N,M = map(int,input().split())
ground = list()
max_square = 0
for n in range(N):
    ground.append(list(map(int,list(input()))))
    max_square = max(max_square,max(ground[n]))
dir_li = [(-1,0),(0,-1),(1,0),(0,1)]
ans = 0
for h in range(1,max_square+1):
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ground[i][j] and ground[i][j]<h and not visited[i][j]:
                ans += bfs(i,j,h)
print(ans)
