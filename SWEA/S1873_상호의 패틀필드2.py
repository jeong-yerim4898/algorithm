
T = int(input()) # 테스트케이스
for tc in range(1,T+1):
    H,W = map(int,input().split()) # 행,열
    mapping = [list(input()) for _ in range(H)]
    dir_li = [(-1,0),(1,0),(0,-1),(0,1)] # ^,v,<,>

    game_dict = {'^':0,'v':1,'<':2,'>':3,'U':0,'D':1,'L':2,'R':3,'S':4,
                 0:'^',1:'v',2:'<',3:'>'} # dir_l인덱스 접근 뿐 아니라 mapping에 표시하기 위한 dictionary

    for i in range(H):
        for j in range(W):
            if mapping[i][j] in ['^','v','<','>']:
                tank_pos = (i,j,game_dict[mapping[i][j]]) # 탱크의 현재 위치와 해당 문자의 dict value
                break # 열 나오고
            else: # 없을 경우 계속 진행
                continue
            break # 행 나오고
    # shoot이랑 이동 나눠서 생각하기
    n = int(input())
    moves = list(input()) # n개의 움직임 들
    for move in moves:
        n_idx = game_dict[move]

        if n_idx ==4: # shoot인 경우
            r = tank_pos[0] # 현재 탱크의 행
            c = tank_pos[1] # 현재 탱크의 열
            while True: # 벽or 맵을 나가기 전까지 직진
                r += dir_li[tank_pos[2]][0]
                c += dir_li[tank_pos[2]][1]
                if r<0 or r>=H or c<0 or c>=W or mapping[r][c]=='#': #map을 벗어나거나 강철벽을 만날경우
                    break
                if mapping[r][c]=='*': # 돌벽을 만날 경우 평지로 바꿈
                    mapping[r][c]='.'
                    break
        else: # 이동하는 경우
            r = tank_pos[0]  # 현재 탱크의 행
            c = tank_pos[1]  # 현재 탱크의 열
            dr = r+dir_li[n_idx][0]
            dc = c+dir_li[n_idx][1]
            mapping[r][c]=game_dict[n_idx] # 강철벽이나 물로 전차가 나갈 수 없는 경우 에도 해당 전차가 향하는 방향을 표시 및 기록해 두어야 한다.
            tank_pos=(r,c,n_idx)
            if -1<dr<H and -1<dc<W and mapping[dr][dc]=='.':
                mapping[r][c]='.'
                mapping[dr][dc]=game_dict[n_idx]
                tank_pos=(dr,dc,n_idx)

        print(f'#{tc}', end=' ')
        for m in mapping:
            print(''.join(m))