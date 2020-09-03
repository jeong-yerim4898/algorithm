def bfs(v):
    q=[]
    visit[v]=1
    q.append(v)
    while q:
        start_p=q.pop(0)
        for next in range(1,N+1):
            if mapping[start_p][next]==1 and visit[next]==0:
                q.append(next)
                visit[next]=visit[start_p]+1
    return




T = 10
for tc in range(1,T+1):
    L, start_p = map(int, input().split())
    data = list(map(int, input().split()))
    case = [data[i:i+2] for i in range(0,L,2)]
    N =max(data)
    mapping = [[0] * (N+1) for _ in range(N+1)]

    for i in range(len(case)):
        mapping[case[i][0]][case[i][1]]=1

    visit = [0] * (N + 1)
    bfs(start_p)

    max_dis = 0
    for l in range(len(visit)):
        if visit[l]>=max_dis:
            max_dis=visit[l]
            idx=l

    print(f'#{tc} {idx}')