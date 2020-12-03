# dfs를 통해 최고 봉우리만 탐색
def dfs(start_r,start_c,h,flag,cnt):
    global ans
    visited[start_r][start_c] =1 # 방문 표시
    if ans< cnt:
        ans = cnt
    for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr = start_r+dir[0]
        nc = start_c+dir[1]
        if -1<nr<N and -1<nc<N and not visited[nr][nc]: # 범위안에 속하고 방문하지 않았다면
            next_h = mapping[nr][nc] # 다음 산의 높이
            if h> next_h: # 현재 봉우리가 다음 봉우리보다 높다면
                dfs(nr,nc,next_h,flag,cnt+1)
                visited[nr][nc]=0
            elif not flag:
                if mapping[nr][nc]-K <h:
                    dfs(nr,nc,h-1,True,cnt+1)
                    visited[nr][nc]=0

T= int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    mapping = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    max_h = max(map(max,mapping)) # 2차원 배열 최댓값
    # 높은 봉오리들 위치 리스트
    start_li = list()
    for i in range(N):
        for j in range(N):
            if mapping[i][j]==max_h:
                start_li.append((i,j))

    # 봉오리 하나 씩 dfs로 확인해보기
    for start in start_li:
        visited = [[0]*N for _ in range(N)]
        dfs(start[0],start[1],max_h,False,1)
    print(f'#{tc} {ans}')
