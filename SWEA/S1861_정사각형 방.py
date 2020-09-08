def bfs(y,x):
    q=[]
    q.append((y,x))

    while q:
        starty,startx = q.pop()
        delta_li = [(0,1),(0,-1),(1,0),(-1,0)]
        for delta in delta_li:
            dy = starty + delta[0]
            dx = startx + delta[1]
            if dx<0 or dx>=N or dy<0 or dy>=N:
                continue
            elif (board[dy][dx]-board[starty][startx])==1:
                q.append((dy,dx))
                visit[board[y][x]]+=1

    return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visit=[0]*(N*N+1)
    max_V =0
    result=list()
    for y in range(N):
        for x in range(N):
            bfs(y,x)

    for i in range(len(visit)):
        if visit[i]==max(visit):
            print(f'#{tc} {i} {visit[i]+1}')
            break