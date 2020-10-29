import sys
sys.setrecursionlimit(100000)

def dfs(r,c,h):
    visited[r][c]=1
    for dir in dir_li:
        nr = r +dir[0]
        nc = c +dir[1]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        elif visited[nr][nc] == 0 and boards[nr][nc] > h:
            dfs(nr, nc,h)




N = int(input())
min_num = 987654321
max_num = 0
boards = [list(map(int,input().split())) for _ in range(N)]
# print(min_num,max_num)
ans=0
dir_li = [(-1,0),(1,0),(0,-1),(0,1)]
for h in range(max(max(boards))):
    visited = [[0]*N for _ in range(N)]
    cnt= 0
    for y in range(N):
        for x in range(N):
            if visited[y][x]==0 and boards[y][x]>h:
                dfs(y,x,h)
                cnt+=1
    ans=max(ans,cnt)
print(ans)
