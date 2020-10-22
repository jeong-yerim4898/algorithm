#dfs

def dfs(i,j,check_point):
    global cnt
    cnt += 1
    visited[i][j]=1
    mapping[i][j]=check_point
    for dir in dir_li:
        ni = i + dir[0]
        nj = j + dir[1]
        if -1<ni<N and -1<nj<N and visited[ni][nj]==0 and mapping[ni][nj]==1:
            dfs(ni,nj,check_point)



N = int(input())
mapping = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
check = list()
dir_li = [(-1,0),(1,0),(0,-1),(0,1)]
check_point = 1
for i in range(N):
    for j in range(N):
        cnt = 0 # 단지별 집의 수를 세기 위한 변수
        if mapping[i][j]==1 and visited[i][j]==0:
            dfs(i,j,check_point)
            check.append(cnt) # 단지별 가구 수 list
            check_point+=1 # 단지 번호 구별

check.sort() # 단지별 가구 수를 오름차순으로
print(len(check))
for i in range(len(check)):
    print(check[i])

