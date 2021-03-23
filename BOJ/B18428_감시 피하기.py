def check_student(r,c):
    for dir in dir_li:
        nr=r
        nc=c
        while -1<nr+dir[0]<N and -1<nc+dir[1]<N:
            nr += dir[0]
            nc += dir[1]
            if board[nr][nc]=='O': #장애물 만났을때
                break
            if board[nr][nc]=='S': #학생을 만난다면
                return True
    return False


def dfs(cnt,idx):
    if cnt==3:
        for t in T_li:
            if check_student(t[0],t[1]):
                return
        print('YES')
        exit()
    for i in range(idx,len(X_li)):
        board[X_li[i][0]][X_li[i][1]]='O' # 장애물 설치
        dfs(cnt+1,i+1)
        board[X_li[i][0]][X_li[i][1]]='X' # 장애물 해체

N = int(input())
board = [list(map(str,input().split())) for _ in range(N)]
checked = [[0]*N for _ in range(N)]
T_li=[] # 선생님 리스트
X_li=[] # 빈곳 리스트
dir_li = [(-1,0),(1,0),(0,-1),(0,1)] #위,아래,왼,오
for i in range(N):
    for j in range(N):
        if board[i][j]=='T':
            T_li.append((i,j))
        if board[i][j]=='X':
            X_li.append((i,j))

dfs(0,0)
print("NO")