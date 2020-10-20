

T = int(input())
for tc in range(1,T+1):
    K = int(input()) # 회전 횟수
    magnets = [list(map(int,input().split())) for _ in range(4)]
    for _ in range(K):
        mag_idx,rot = map(int,input().split())
        mag_idx -=1 # 톱니바퀴 인덱스 맞추기 위해 0~3 톱니바퀴
        move = [(mag_idx,rot)] # 움직이는 경로 리스트

        # 왼쪽 확인
        tmp_rot = rot
        for i in range(mag_idx-1,-1,-1):
            if magnets[i][2] != magnets[i+1][6]: # 기준 왼쪽, 기준
                tmp_rot*=-1 # 극이 다르면 방향 바꾸기
                move.append((i,tmp_rot))
            else: #같으면 회전하지 않는다.
                break # 반복문 끝낸다. 왼쪽 탐색중 하나라도 회전하지 않으면 더 확인할 필요가 없다.
        #오른쪽 확인
        tmp_rot = rot
        for i in range(mag_idx+1,4):
            if magnets[i][6]!=magnets[i-1][2]:
                tmp_rot*=-1
                move.append((i,tmp_rot))
            else:
                break
        # move 리스트를 기반으로 톱니 돌리기
        for idx,rot in move:
            if rot ==1: # 시계방향
                value = magnets[idx].pop()
                magnets[idx].insert(0,value)
            else:
                value = magnets[idx].pop(0)
                magnets[idx].append(value)
        # print(magnets)
    # 결과값
    ans = 0
    for i in range(4):
        ans+= magnets[i][0]*(2**i)

    print(f'#{tc} {ans}')