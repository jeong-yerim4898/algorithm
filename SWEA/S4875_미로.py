def condition(y,x):
    return 0<=y<N and 0<=x<N and(miro[y][x]=='0' or miro[y][x]=='3')

def escape(y,x):
    global result

    if miro[y][x] == '3':
        result = 1
        return
    visited.append((y, x))
    for delta in delta_li:
        dy = y + delta[0]
        dx = x + delta[1]
        if condition(dy,dx) and (dy,dx) not in visited:
            escape(dy,dx)





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    visited = list()
    result = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j]=='2':
                start_y = i
                start_x = j
    delta_li= [(-1,0),(1,0),(0,-1),(0,1)]
    escape(start_y,start_x)
    print(f'#{tc} {result}')
