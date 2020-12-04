def dijkstra(start,weight):
    pass


N,M,S,E = map(int,input().split())
mapping=[[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    a,b,dis,f1,f2=map(int,input().split())
    mapping[a][b]=(dis,f1) #f1 a에서 b까지 정체유뮤
    mapping[b][a]=(dis,f2) #f2 b에서 a까지 정체우뮤
start = 1
wight= mapping[start][:]
result = dijkstra(start,weight)