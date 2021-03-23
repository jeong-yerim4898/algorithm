def dfs(now,last,wire):
    global maxcores,minwire
    if maxcores<len(now):
        maxcores=len(now)
        minwire=978654321
    if maxcores==len(now) and minwire>wire:
        minwire=wire
    for i in range(last,len(cores)):
        for dir in dir_li:
            plus = connect(cores[i][0],cores[i][1],dir)
            if not plus: #연결
                continue
            next = now[:]
            next.append(i)
            dfs(next,i+1,wire+plus)
            cancel(cores[i][0],cores[i][1],plus,dir)

def cancel(r,c,cnt,dir):
    for _ in range(cnt):
        board[r+dir[0]][c+dir[1]]=0
        r+=dir[0]
        c+=dir[1]

def connect(r,c,dir):
    now_r,now_c=r,c
    w_cnt=0
    while -1<r+dir[0]<N and -1<c+dir[1]<N:
        r += dir[0]
        c+= dir[1]
        if board[r][c]:
            break
        board[r][c]=2 #와이어 연결
        w_cnt+=1 #와이어 개수 추가
    else: # 정해진 자리 벗어난 경우
        return w_cnt
    cancel(now_r,now_c,w_cnt,dir) # 전선취소
    return 0

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    checked = [[0]*N for _ in range(N)]
    dir_li = [(-1,0),(1,0),(0,-1),(0,1)]
    cores = []
    fix=1
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                if i==0 or i==N-1 or j==0 or j==N-1: #가장자리 연걸
                    fix+=1
                else:
                    cores.append((i,j))
    maxcores=-1
    minwire=987654312
    dfs([],0,0)
    print('#'+str(tc),minwire)