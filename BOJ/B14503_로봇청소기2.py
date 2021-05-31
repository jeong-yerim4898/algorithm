from collections import deque
def clean_room(r,c,d):
    cnt=1 #현재 위치 청소 완료
    q = deque()
    q.append([r,c])
    board[r][c]=2 #1벽 0빈칸

    while q:
        cr,cc = q.popleft() #현재위치
        for i in range(4):
            d = (d + 3) % 4 #왼쪽으로 회전
            nr = cr + dir_li[d][0]
            nc = cc + dir_li[d][1]
            if 0 <= nr <N and 0 <= nc < M and board[nr][nc] == 0:
                q.append([nr, nc])
                cnt += 1
                board[nr][nc] = 2
                break
            if i == 3:  # 갈 곳이 없다.
                nr=cr + dir_li[(d + 2) % 4][0] #뒤 방향
                nc = cc + dir_li[(d + 2) % 4][1]
                q.append([nr,nc])
                if board[nr][nc] == 1: # 뒤로 갔는데 벽이면
                    return cnt

N,M = map(int,input().split()) #세로,가로
r,c,d = map(int,input().split()) #현재 위치방향
dir_li = [(-1,0),(0,1),(1,0),(0,-1)] # 북 동 남 서
board = [list(map(int,input().split())) for _ in range(N)]
print(clean_room(r,c,d))