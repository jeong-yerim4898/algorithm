from collections import defaultdict,deque
def dfs(node):
    print(node,end=' ')
    dfs_check[node]=True
    for next_node in board[node]:
        if not dfs_check[next_node]:
            dfs_check[next_node] = True
            dfs(next_node)
def bfs(node):
    q = deque()
    q.append(node)
    check=[False]*(N+1) #방문체크
    check[node]=True
    print(node,end=' ')
    while q:
        node = q.popleft()
        for next_node in board[node]:
            if not check[next_node]:
                check[next_node]=True
                q.append(next_node)
                print(next_node,end=' ')

N,M,V = map(int,input().split()) #정점,간선,시작점
board = defaultdict(list)
dfs_check=[False]*(N+1)
for _ in range(M):
    s,e = map(int,input().split())
    board[s].append(e)
    board[e].append(s)
for m in range(N+1):
    board[m].sort()
dfs(V)
print()
bfs(V)

