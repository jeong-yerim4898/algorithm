def bfs(s):
    global result
    q=[]
    visit=[0]*(V+1)
    q.append(s)
    visit[s]=1

    while q:
        start_n=q.pop(0)

        for i in range(1,V+1):
            if mapping[start_n][i]==1 and visit[i]==0:
                q.append(i)
                visit[i]=visit[start_n]+1
                if i == end_n:
                    result = visit[i]-1
                    return
    result
    return

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    mapping = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s,e = map(int,input().split())
        mapping[s][e]=1
        mapping[e][s]=1
    start_n,end_n =map(int,input().split())
    result = 0
    bfs(start_n)
    print(f'#{tc} {result}')