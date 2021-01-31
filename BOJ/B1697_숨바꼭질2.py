#bfs
from collections import deque
def bfs(n):
    q=deque([n])
    while q:
        n = q.popleft()
        if n==K:
            print(visited[n])
            return
        for next in (n-1,n+1,n*2):
            if -1<next<100001 and visited[next]==0:
                visited[next]=visited[n]+1
                q.append(next)
N,K = map(int,input().split())
visited=[0]* 100001
bfs(N)