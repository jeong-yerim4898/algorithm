def bfs(s):
    global F,S,G,U,D,min_cnt,tmp_cnt
    q =list()
    q.append(s)
    visited[s]=1
    while q:
        now_floor= q.pop(0)
        if now_floor==G:
            print(visited[now_floor]-1)
            return
        for i in range(len(dir_li)):
            next_floor = now_floor+dir_li[i]
            if 1<=next_floor<=F and not visited[next_floor]:
                q.append(next_floor)
                visited[next_floor]= visited[now_floor]+1
    print('use the stairs')

F,S,G,U,D = map(int,input().split())
visited = [0]*(F+1)
dir_li = [U,-D]

bfs(S)
