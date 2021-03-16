def dfs(node):
    global cnt
    visit[node]=1
    if node==N+1:
        return cnt
    for i in range(1,N+1):
        if board[node][i] and not visit[i]:
            cnt+=1
            dfs(i)


N = int(input()) #노드 번호
M = int(input()) # 간선 갯수
board = [[0]*(N+1) for _ in range(N+1)]
visit = [0]*(N+1)
for _ in range(M):
    r,c = map(int,input().split())
    board[r][c]=1
    board[c][r]=1
cnt=0
dfs(1)
print(cnt)