def prim(adj,start):
    INF = float('inf') # 어떤 숫자 비교해도 가장 큰수
    st = [0]*(V+1)  # 출발 정점
    weight = [INF]*(V+1) # 정점을 선택하기 위한 가중치를 저장하는 배열
    mst = [0]*(V+1) # 각 정점이 mst에 포함되어 있는지(1) 아닌지(0)
    weight[start]=0
    result = 0 # 가중치의 합을 구하기 위한 변수

    #mst에 모든 정점이 선택 될 때 까지 반보
    for _ in range(V+1):
        min_w = INF
        min_v = 0
        for i in range(V+1):
            # 정점이 mst에 미포함이면서 가중치가 가장 작아야 함.
            if mst[i]==0 and weight[i]<min_w:
                min_w = weight[i]
                min_v = i 
        #갈 수 있는 정점중 가장 작은 경로 선택
        mst[min_v]=1
        result += min_w

        # 새로 선택한 정점으로 부터 갈 수 있는 경로를 살펴보고
        # 노드를 선택하기 위한 정점의 가중치가 작아지면, 수정
        for i in range(V+1):
            if adj[min_v][i]>0 and not mst[i] and adj[min_v][i]<weight[i]:
                weight[i]= adj[min_v][i]
                st[i]= min_v

    # print(st)
    # print(weight)
    return result

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w

    result = prim(adj,0)
    print(f'#{tc} {result}')