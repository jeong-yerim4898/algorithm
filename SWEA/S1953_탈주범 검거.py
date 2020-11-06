from collections import deque

def bfs(r,c):
    global cnt
    q= deque([(r,c)])
    visitied[r][c]=1
    while q:
        y,x = q.popleft()
        for dir in dir_dic[basement[y][x]]:
            ny =y +dir[0]
            nx =x +dir[1]
            if 0<=ny<N and 0<= nx<M and not visitied[ny][nx] and basement[ny][nx]:
                if (-dir[0],-dir[1]) in dir_dic[basement[ny][nx]]: # 지금 관과 다음 관과 연결되어 있는가
                    visitied[ny][nx]=visitied[y][x]+1
                    q.append((ny,nx))
                    if visitied[ny][nx]<=L: # 제한 시간보다 적은가
                        cnt+=1




T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    #세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L
    basement = [list(map(int,input().split())) for _ in range(N)]
    visitied = [[0]*M for _ in range(N)]
    dir_dic = {
        1:[(-1,0),(0,1),(1,0),(0,-1)] ,# 위 오 아래 왼
        2:[(-1,0),(1,0)], #위 아래
        3:[(0,-1),(0,1)] ,# 왼 오
        4:[(-1,0),(0,1)] ,# 위 오
        5:[(0,1),(1,0)], #아래 오
        6:[(1,0),(0,-1)], # 왼 아래
        7:[(0,-1),(-1,0)] #왼 위
    }
    cnt = 1
    bfs(R,C)
    print(f'#{tc} {cnt}')