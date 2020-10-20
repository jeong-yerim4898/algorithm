def dfs(start_node):
    print(start_node,end = " ")
    visited[start_node] = 1
    for i in range(1, N + 1):
        if visited[i] == 0 and mapping[start_node][i]:
            visited[i] = 1
            dfs(i)

def bfs(start_node):

    print(start_node,end=" ")
    q = list()
    visited = [0]*(N+1)
    q.append(start_node)
    visited[start_node]=1
    while q:
        s_node = q.pop(0)
        for i in range(1,N+1):
            if visited[i] == 0 and mapping[s_node][i]:
                q.append(i)
                visited[i]=1
                print(i,end=" ")

N,M,V = map(int,input().split()) # 정점 개수, 간선의 개수,시작 정점 번호
mapping = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    s,e = map(int,input().split())
    mapping[s][e]=1
    mapping[e][s]=1

dfs(V)
print()
bfs(V)
