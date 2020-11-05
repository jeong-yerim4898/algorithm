#dijkstra

def dijkstra(mapping):
    INF = float('inf')
    weight = [[INF]*N for _ in range(N)] # 연료 사용량 저장할 공간
    trust = [[False]*N for _ in range(N)]  # 확실히 지나는 경우
    weight[0][0] = 0 # 출발점에서 연료를 사용하지 않는다.
    U = set()
    U.add((0,0))
     # 현재 방문하지 않은 정점중 최소비용으로 방문 할 수 있는 곳
    while True:
        min_w = INF
        for r,c in U:
            if weight[r][c]<min_w and not trust[r][c]:
                min_w = weight[r][c]
                y,x = r,c

        trust[y][x]=True # 확실한 정점으로 체크해주기
        U.remove((y,x))  # 다음으로 최소가 되는 행렬 위치 더해주기
        if y==x==N-1:
            print(weight)
            return weight[y][x]

        for dir in dir_li:
            ny,nx = y+dir[0], x+dir[1]
            if 0<=ny<N and 0<=nx<N and not trust[ny][nx]:
                if mapping[ny][nx]>mapping[y][x]:
                    fuel = weight[y][x]+(mapping[ny][nx]-mapping[y][x]+1)
                else:
                    fuel = weight[y][x]+1

                if fuel<weight[ny][nx]:
                    weight[ny][nx]=fuel
                    U.add((ny,nx))

T =int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping = [list(map(int,input().split())) for _ in range(N)]
    # print(mapping)
    dir_li = [(-1,0),(0,1),(1,0),(0,-1)]

    print(f'#{tc} {dijkstra(mapping)}')