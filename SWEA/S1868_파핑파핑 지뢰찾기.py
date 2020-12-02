# 주변에 지뢰가 없는 경우 먼저 발견하기
from collections import deque
def eightorpass(r,c): # 팔방에 없거나 하나라도 있으면 pass
    global cnt
    next_ele = list()
    for d in range(8):
        nr = r+dr[d]
        nc = c+dc[d]
        if -1<nr<N and -1<nc<N:
            if mapping[nr][nc] == '.':
                next_ele.append((nr,nc))
            elif mapping[nr][nc]=='*': # 지뢰가 있는 경우
                break
    else: # break를 만나지 않았다. 즉, 8방에 지뢰가 없다.
        if next_ele: #다음 갈 곳이 있다면
            mapping[r][c]=True # 방문 체크하고
            cnt+=1 # cnt하나 더해 준다.
            bomb(next_ele)

def bomb(q): # 최초 클릭 장소를 알고 그다음 퍼져 나가는걸 알아보는 함수
    next_q = deque(q)
    while next_q:
        r,c = next_q.popleft()
        mapping[r][c]=True
        next_next_q = list()
        for i in range(8): #8방확인
            nr = r + dr[i]
            nc = c + dc[i]
            if -1<nr<N and -1<nc<N:
                if mapping[nr][nc] == '.':
                    next_next_q.append((nr, nc))
                elif mapping[nr][nc] == '*':  # 지뢰가 있는 경우
                    break
        else:
            bomb(next_next_q)




T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 변의 길이
    mapping = [list(input()) for _ in range(N)]
    cnt = 0
    dr = [-1,-1,-1,0,1,1,1,0]
    dc = [-1,0,1,1,1,0,-1,-1]

    for i in range(N): # 행
        for j in range(N): # 열
            if mapping[i][j]=='.':
                eightorpass(i,j)
    # 클릭했을때 하나만 터지는 경우 들
    for m in range(N):
        for l in range(N):
            if mapping[m][l]=='.':
                cnt+=1
    print(f'#{tc} {cnt}')