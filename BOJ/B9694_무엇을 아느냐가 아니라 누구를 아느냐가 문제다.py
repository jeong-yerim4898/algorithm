import heapq
import sys
input = sys.stdin.readline
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    # 본인의 거리는 0
    distance[start]=0
    while q:
        # 가장 최단 거리 노드에 대한 정보
        dist,now = heapq.heappop(q)
        # 꺼낸 거리가 더 크다면 continue
        if distance[now]<dist:
            continue
        for pos,c in graph[now]:
            cost = dist + c
            if cost<distance[pos]:
                path[pos] = now
                distance[pos]=cost
                heapq.heappush(q,(cost,pos))
T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split()) #관계수(간선수), 정치인 수(노드수)
    graph = [[] for _ in range(M)]
    distance = [int(1e9) for _ in range(M)]
    path = [-1 for _ in range(M)]
    # 모든 간선의 정보 입력받기
    for _ in range(N):
        s,e,cost = map(int,input().split())
        # 양방향
        graph[s].append((e,cost))
        graph[e].append((s,cost))
    # 0번 인덱스가 한신이 본인
    dijkstra(0)
    result = [M - 1]
    idx = M - 1
    while path[idx] != -1:
        idx = path[idx]
        result.append(idx)
    result.reverse()
    if len(result) == 1:
        result = [-1]
    print('Case #'+str(tc)+':', *result)
