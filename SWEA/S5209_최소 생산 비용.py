def dfs(y):
    global min_result,tmp_result
    if y == N:
        if tmp_result<= min_result:
            min_result=tmp_result
        return
    if min_result<=tmp_result:
        return
    for x in range(N):
        if not visited[x]:
            visited[x]=1
            tmp_result+=factory[y][x]
            dfs(y+1)
            visited[x]=0
            tmp_result-=factory[y][x]


T = int(input())
for tc in range(1,T+1):
    N = int(input()) #제품수
    factory = [list(map(int,input().split())) for _ in range(N)]
    visited= [0]*N
    tmp_result = 0
    min_result = 987654321
    dfs(0)
    print(f'#{tc} {min_result}')