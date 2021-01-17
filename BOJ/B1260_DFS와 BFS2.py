from collections import deque
def dfs(node):
    print(node,end=' ')
    visited[node]=1
    for n in range(1,N+1):
        if visited[n]==0 and mapping[node][n]==1:
            visited[n]=1
            dfs(n)

def bfs(node):
    q = deque([node])
    visited=[0]*(N+1)
    visited[node]=1
    print(node,end=' ')
    while q:
        node = q.popleft()
        for n in range(1,N+1):
            if visited[n]==0 and mapping[node][n]==1:
                visited[n]=1
                q.append(n)
                print(n,end=' ')

N,M,V = map(int,input().split())
mapping = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    s,e = map(int,input().split())
    mapping[s][e]=1
    mapping[e][s]=1 #방향이 양방향 가능
dfs(V)
print()
bfs(V)