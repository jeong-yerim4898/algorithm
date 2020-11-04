# BFS
'''
6 5
1 2
1 3
3 4
2 3
4 5
'''
from collections import deque
def bfs(s_node):
    q = deque([s_node])
    visited[s_node]=1
    while q:
        node = q.popleft()
        for n_node in range(1,N+1):
            if not visited[n_node] and mapping[node][n_node]==1:
                visited[n_node]+=visited[node]+1
                q.append(n_node)
    return visited
T = int(input())
for tc in range(1,T+1):
    N ,M = map(int,input().split()) #친구수, 관계수
    mapping = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        s , e = map(int,input().split())
        mapping[s][e] = 1
        mapping[e][s]= 1

    bfs(1)
    cnt=0
    for i in visited:
        if i ==2 or i ==3:
            cnt+=1
    print(f'#{tc} {cnt}')