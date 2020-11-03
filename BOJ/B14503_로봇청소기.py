def bfs(r, c, d):
    cnt = 1
    q = list()
    q.append([r, c])
    maru[r][c] = 2  # 벽1 바닥0

    while q:
        dr, dc = q.pop(0)
        for i in range(4):
            d = (d + 3) % 4
            nr = dr + dir_li[d][0]
            nc = dc + dir_li[d][1]
            # 왼쪽 방향 청소가능 할 때
            if 0 <= nr <N and 0 <= nc < M and maru[nr][nc] == 0:
                q.append([nr, nc])
                cnt += 1
                maru[nr][nc] = 2
                break

            if i == 3:  # 갈 곳이 없다.
                nr=dr + dir_li[(d + 2) % 4][0]
                nc = dc + dir_li[(d + 2) % 4][1]
                q.append([nr,nc])
                if maru[nr][nc] == 1:
                    return cnt

N,M = map(int,input().split()) #세로, 가로
r,c,d = map(int,input().split()) # 시작점r,c / 방향 d
maru = [list(map(int,input().split())) for _ in range(N)]
dir_li = [(-1,0),(0,1),(1,0),(0,-1)] #북0 동1 남2 서3   행열


print(bfs(r,c,d))



