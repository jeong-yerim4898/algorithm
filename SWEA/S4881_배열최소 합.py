

def dfs(y):
    global min_result
    global result
    if y == N:
        if result<=min_result:
            min_result=result
        return
    for x in range(N):
        if visited[x]==0:
            visited[x]=1
            result+=board[y][x]
            if min_result > result:
                dfs(y+1)
            visited[x] = 0
            result-=board[y][x]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    min_result = 987654321
    result = 0
    dfs(0)
    print(f'#{tc} {min_result}')
