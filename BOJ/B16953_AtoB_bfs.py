from collections import deque
def bfs(n):
    global ans
    q = deque()
    q.append((n,1))
    while q:
        a,depth = q.popleft()
        if a==B:
            ans=depth

            break
        if a*2<=B:
            q.append((a*2,depth+1))
        if int(str(a)+'1')<=B:
            q.append((int(str(a)+'1'),depth+1))

A,B = map(int,input().split())
ans=-1
bfs(A)
print(ans)