def dfs(start,next, cost,cnt):
    global min_cost
    if (start==next) and cnt==N:
        if min_cost>cost:
            min_cost = cost
            return
    for i in range(N):
        if case[next][i]!=0 and visited[i]==0:
            visited[i]=1
            cost+=case[next][i]
            if cost<=min_cost:
                dfs(start,i,cost,cnt+1)
            visited[i]=0
            cost-=case[next][i]


N = int(input())
case = [list(map(int,input().split())) for _ in range(N)]
visited= [0]*N
min_cost = 987654321
for j in range(N):
    dfs(j,j,0,0)
print(min_cost)