def bfs(y,x):
    delta_li = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    Q = [(y,x)]
    ground[y][x]=0
    cntt =1
    while Q:
        a,b = Q.pop()
        for delta in delta_li:
            dy = a +delta[0]
            dx = b + delta[1]
            if 0<=dy<N and 0<=dx<M and ground[dy][dx]==1:
                ground[dy][dx]=0
                Q.append((dy,dx))
                cntt+=1
    cnt.append(cntt)
T = int(input())
for tc in range(T):
    M,N,K = map(int,input().split())
    ground = [[0] * M for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    cnt = []
    for y in range(N):
        for x in range(M):
            if ground[y][x]==1:
                bfs(y,x)
    print(len(cnt))