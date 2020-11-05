def dijkstra(start,road,weight):
    U= {start} # 방문 할때 마다 정점을 추가
    while len(U)<V:

        # 현재 방문하지 않은 정점 중, 최소 비용으로 방문 할 수 있는 정점 방문
        min_w = INF
        min_idx = -1
        for i in range(V):
            if i not in U and weight[i]<min_w:
                min_w = weight[i]
                min_idx=i
        U.add(min_idx)

        # 새로운 정점을 방문하고 나서 그 정점으로 부터 갈 수 있는 모든 정점의 비용을 확인해서 기존 최소 비용보다 더 작다면 수정
        for i in range(V+1):
            if i not in U:
                # 방금 선택한 노드에서 i노드로 가는 길이가
                # 기존에 i로 가는 비용보다 저렴하다면 업데이트하기
                tmp = min_w+road[min_idx][i]
                if weight[i]>tmp:
                    weight[i]=tmp

    return weight


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    INF = float('inf')
    road = [[INF]*(V+1) for _ in range(V+1)] # 처음부터 inf로 가장 큰 값을 넣어줌
    for i in range(E):
        s,e,w = map(int,input().split())
        road[s][e] = w
    start = 0
    weight = road[start][:] #후보가 되는 모든 부분은 가지고 와버림 (0번 행)
    result = dijkstra(start,road,weight)
    print(f'#{tc} {result[-1]}')
