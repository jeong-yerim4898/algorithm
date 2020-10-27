# bfs
from collections import deque
def bfs():
    global sister
    q =deque()
    q.append(subin)
    while q:
        node = q.popleft()
        if node == sister:
            print(visited[node])
            return
        else:
            for next_node in (node-1,node+1,node*2):
                if 0<=next_node<1000001 and not visited[next_node]:
                    visited[next_node]=visited[node]+1
                    q.append(next_node)


subin, sister = map(int,input().split())
visited = [0]*1000001
cnt = 0
bfs()