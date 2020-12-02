

T = int(input()) # testcase 수
for tc in range(1,T+1):
    H,W = map(int,input().split()) # H 높이(행) W 열
    mapping = [list(input()) for _ in range(H)]
    keyboard = ['<','>','^','v']
    dir_li = [(-1,0),(1,0),(0,-1),(0,1)] #^,v,<,> (열,행)

    command_dic = {'U': 0, 'D': 1, 'L': 2, 'R': 3, 'S': 4,
                    '^': 0, 'v': 1, '<': 2, '>': 3, 0: '^', 1: 'v', 2: '<', 3: '>'}

    for i in range(H): # 행
        for j in range(W):# 열
            if mapping[i][j] in keyboard:
                tank_pos = (i,j,command_dic[mapping[i][j]])
                break # 위치 찾았으면 나가기
            else:
                continue
            break
    n =input()
    commands= list(input())
    for command in commands:
        tmp = command_dic[command]
        if tmp==4: #발사
            dr = tank_pos[0] #탱그의 현 행
            dc = tank_pos[1] #탱크의 현 열
            while True:
                dr += dir_li[tank_pos[2]][0] #행 더하기
                dc += dir_li[tank_pos[2]][1] #열 더하기
                #범위 벗어나고 강철 벽을 만날경우 무효화
                if dr<0 or dr>=H or dc<0 or dc>=W or mapping[dr][dc]=='#':
                    break
                # 돌벽을 만난다면
                if mapping[dr][dc]=='*':
                    mapping[dr][dc]='.'
                    break #돌벽을 평지로 만들고 포탄은 무효화
        else: #이동 명령
            r = tank_pos[0]
            c = tank_pos[1]
            dr = r + dir_li[tmp][0]
            dc = c + dir_li[tmp][1]
            mapping[r][c] = command_dic[tmp]
            tank_pos=(r,c,tmp)
            if -1<dr<H and -1<dc<W and mapping[dr][dc]=='.':
                mapping[r][c]='.'
                #가야하는 위치에 탱크 표시
                mapping[dr][dc]= command_dic[tmp]
                tank_pos=(dr,dc,tmp)
    print(f'#{tc}',end=' ')
    for m in mapping:
        print(''.join(m))
