def bfs(node):
    global p2
    q=list()
    visited=[0]*(N+1)
    q.append(node)
    visited[node]=1

    while q:
        s_node = q.pop(0)
        for i in range(1,N+1):
            if visited[i]==0 and mapping[s_node][i]==1:
                q.append(i)
                visited[i]=visited[s_node]+1
                if i == p2:
                    return visited[i]-1
    return -1


N = int(input()) # 전체 사람수
p1,p2 = map(int,input().split()) # 대상 자1,2
n = int(input()) # 관계 수
mapping = [[0]*(N+1) for _ in range(N+1)]
for _ in range(n):
    p,c = map(int,input().split())
    mapping[p][c]=1
    mapping[c][p]=1

print(bfs(p1))