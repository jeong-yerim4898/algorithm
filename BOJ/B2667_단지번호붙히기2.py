def bfs(r,c):
    n=1
    q =list()
    q.append([r,c])
    mapping[r][c]=0
    while q:
        r,c =q.pop()
        for dir in dir_li:
            nr=r+ dir[0]
            nc=c+dir[1]
            if -1<nr<N and -1<nc<N and mapping[nr][nc]==1:
                    n+=1
                    mapping[nr][nc]=0
                    q.append([nr,nc])
    return n

N = int(input())
mapping = [list(map(int,input())) for _ in range(N)]
ans_li = list()
dir_li = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(N):
    for j in range(N):
        if mapping[i][j]==1:
            ans_li.append(bfs(i,j))

print(len(ans_li))
for ans in sorted(ans_li):
    print(ans)