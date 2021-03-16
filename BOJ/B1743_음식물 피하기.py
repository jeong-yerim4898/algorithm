from collections import deque
def bfs(r,c):
    trash = 1
    q= deque()
    q.append((r,c))
    checked[r][c]=1
    while q:
        r,c = q.popleft()
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+ dir[0]
            nc = c+dir[1]
            if -1<nr<N and -1<nc<M:
                if not checked[nr][nc] and passage[nr][nc]:
                    trash+=1
                    checked[nr][nc]=1
                    q.append((nr,nc))
    return trash



N,M,K = map(int,input().split())
passage = [[0]*M for _ in range(N)]
checked = [[0]*M for _ in range(N)]
max_val = -98765431
for t in range(K):
    r,c = map(int,input().split())
    passage[r-1][c-1]=1
ans_li=[]
for i in range(N):
    for j in range(M):
      if passage[i][j] and not checked[i][j]:
          ans = bfs(i,j)
          ans_li.append(ans)
print(max(ans_li))