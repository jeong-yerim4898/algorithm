# 양방향 bfs
def bfs(v):
    global ans
    Q = list()
    Q.append(v)
    while Q: # 큐가 빌때 까지
        v= Q.pop(0)
        for w in graph[v]:
            if not visit[w]:
                Q.append(w)
                visit[w]=visit[v]+1
                ans+=1



node = int(input())
n = int(input())
graph = [[] for _ in range(node+1)]
visit = [0]*(node+1)
ans = 0
for _ in range(n):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(1) # 1노드 부터 시작
print(ans-1)