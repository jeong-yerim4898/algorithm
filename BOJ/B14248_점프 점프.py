
def bfs(stone,dis):
    global cnt
    q=[(stone,dis)]
    visited[stone]=1
    while q:
        stone,dis = q.pop(0)
        for i in range(2):
            dis= dis*-1
            n_stone = stone+dis
            if -1<n_stone<n and visited[n_stone]==0:
                visited[n_stone]=1
                q.append((n_stone,stones[n_stone]))
                cnt+=1

n = int(input())
stones = list(map(int,input().split()))
s = int(input())
s= s-1
cnt =1
visited = [0]*n
dis = stones[s]
bfs(s,dis)
print(cnt)

