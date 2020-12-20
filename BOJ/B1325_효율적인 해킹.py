import sys
from collections import deque
input = sys.stdin
def bfs(s):
    global cnt
    q= deque()
    visited=[0]*(N+1)
    visited[s]=1
    q.append(s)
    cnt=1
    while q:
        i = q.popleft()
        for j in mapping[i]:
            if not visited[j]:
                q.append(j)
                visited[j]=1
                cnt+=1
    return cnt
N,M =map(int,input.readline().split())
mapping = [[] for _ in range(N+1)]
ans =[]
for _ in range(M):
    a,b = map(int,input.readline().split())
    mapping[b].append(a)
tmp_m=-1
for k in range(1,N+1):
    current = bfs(k)
    if current==tmp_m:
        ans.append(k)
    elif current>tmp_m:
        ans = [k]
        tmp_m=current
for e in ans:
    print(e,end=' ')