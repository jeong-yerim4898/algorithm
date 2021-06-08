import heapq
import sys
input = sys.stdin.readline

def dijkstra(board,start,N):
    distance = [int(1e9) for _ in range(N + 1)]
    q =[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 가장 최단 거리 노드에 대한 정보
        now_dist, now_node = heapq.heappop(q)
        if distance[now_node]<now_dist:
            continue
        for next_node,next_dist in board[now_node]:
            cost = now_dist + next_dist
            if cost<distance[next_node]:
                distance[next_node]=cost
                heapq.heappush(q,(cost,next_node))
    return distance

N,M,X = map(int,input().split()) #노드의수, 간선의 수, 목적지
graph = [[] for _ in range(N+1)]
re_graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,cost = map(int,input().split())
    # 정방향
    graph[s].append((e,cost))
    # 역방향
    re_graph[e].append((s,cost))
ans = -98765431
go = dijkstra(graph,X,N) # 파티장소 -> 각 마을
back = dijkstra(re_graph,X,N) #각 마을 -> 파티장소
for i in range(1,N+1):
    ans = max(ans,go[i]+back[i])
print(ans)