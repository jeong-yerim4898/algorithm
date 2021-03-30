#단방향
import sys
from collections import defaultdict,deque
def bfs(node):
    q = deque()
    q.append((node,0))
    check = [False]*(N+1)
    check[node]=True
    while q:
        current,step = q.popleft()
        if step == K:
            ans.append(current)
            continue
        elif step<K:
            for i in board[current]:
                if not check[i]:
                    check[i]=True
                    q.append((i,step+1))
input = sys.stdin.readline
N,M,K,X = map(int,input().split()) # 도시개수,도로개수,거리정보,출발도시 번호
board = defaultdict(list)
for _ in range(M):
    s,e = map(int,input().split())
    board[s].append(e)
ans=list()
bfs(X)
if len(ans)==0:
    print(-1)
else:
    for a in sorted(ans):
        print(a)
