import sys
sys.setrecursionlimit(100000)

def dfs(r,c):
    visited[r][c]=1
    for dir in dir_li:
        nr = r +dir[0]
        nc = c +dir[1]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        elif visited[nr][nc] == 0 and boards[nr][nc] > h:
            dfs(nr, nc)




N = int(input())
min_num = 987654321
max_num = 0
boards = [list(map(int,input().split())) for _ in range(N)]

# print(min_num,max_num)
ans=list() # 높이마다 안전구역의 값들을 모은다.
dir_li = [(-1,0),(1,0),(0,-1),(0,1)]
for h in range(max(max(boards))): # 높이를 기준으로 경우를 확인한다.
    visited = [[0]*N for _ in range(N)]
    cnt= 0 # 안전구역을 값을 저장하는 변수
    for y in range(N):
        for x in range(N):
            if visited[y][x]==0 and boards[y][x]>h:
                dfs(y,x)
                cnt+=1
    ans.append(cnt)
if len(ans) == 0: # 안전 구역이 없는 경우도 있다.
    print(0)
else:
    print(max(ans))
