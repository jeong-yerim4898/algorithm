from collections import deque
def bfs(node):
    global cnt
    q=deque([node])
    visited = [0]*(N+1)
    visited[node]=1
    while q:
        node = q.popleft()
        for next_node in range(1,N+1):
            if mapping[node][next_node]==1 and not visited[next_node]:
                visited[next_node]=1
                q.append(next_node)
                cnt+=1

N= int(input())
pair = int(input())
mapping = [[0]*(N+1) for _ in range(N+1)]
for _ in range(pair):
    s,e = map(int,input().split())
    mapping[s][e]=1
    mapping[e][s]=1
cnt=0
bfs(1)
print(cnt)