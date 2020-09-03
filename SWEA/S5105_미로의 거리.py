
def bfs(i,j):
    d_li=[(-1,0),(1,0),(0,-1),(0,1)]
    queue = list()
    queue.append((i,j,0))
    while queue:
        ci,cj,length = queue.pop(0)
        visited[ci][cj] = 1

        for d in d_li:
            ni = ci + d[0]
            nj = cj + d[1]
            if 0<= ni <L and 0<= nj < L and not visited[ni][nj]:
                if maze[ni][nj] == 0:
                    queue.append((ni,nj,length+1))
                elif maze[ni][nj] == 3:
                    return length
    return 0

def f():
    for i in range(L):
        for j in range(L):
            if maze[i][j] == 2:
                return bfs(i,j)


T = int(input())
for tc in range(1,T+1):
    L = int(input())
    maze = [list(map(int,input())) for _ in range(L)]
    visited = [[0] * L for _ in range(L)]
    result = f()
    print("#{} {}".format(tc,result))

