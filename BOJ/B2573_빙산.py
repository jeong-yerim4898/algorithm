# bfs로 1년마다 0 갯수만큼 높이 줄이기
# 4방 확인후 dfs로 덩어리 확인
from collections import deque
from sys import exit

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    year_sea = list() #년마다 존재하는 빙산과 둘러쌓인 바다

    while q:
        qi,qj = q.popleft()
        sea_cnt = 0
        for dir in dir_li:
            ni = qi + dir[0]
            nj = qj + dir[1]
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                if icies[ni][nj]==0:
                    sea_cnt +=1
                else:
                    visited[ni][nj] = 1
                    q.append((ni,nj))
        year_sea.append((qi,qj,sea_cnt))

    return year_sea

N,M = map(int,input().split()) #행 열
icies = [list(map(int,input().split())) for _ in range(N)]
dir_li = [(-1,0),(0,1),(1,0),(0,-1)]

year = 0
while True:
    visited = [[0]*M for _ in range(N)]
    ice = deque()
    cnt = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if icies[i][j] >0 and not visited[i][j]: # 녹일수 있는 빙산의 위치
                cnt+=1
                if cnt>1:
                    print(year)
                    exit()
                ice.extend(bfs(i,j))
    if cnt==0:
        year = 0
        break
    year+=1

    while ice:
        i,j,h = ice.popleft()
        icies[i][j] = max(0,icies[i][j]-h)
print(year)


