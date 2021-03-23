import copy
N,M,r,c,K = map(int,input().split()) #세로, 가로,r,명령의 개수
board=[list(map(int,input().split())) for _ in range(N)] # 지도
dir = [(0,1),(0,-1),(-1,0),(1,0)] #동서북남
#[위,동,서,북,남,바]
dice_idx=[[2,0,5,3,4,1],[1,5,0,3,4,2],[4,1,2,0,5,3],[3,1,2,5,0,4]] #동서북남으로 위치한 주사위의 index
dice = [0]*6 #처음 주사위 값들은 다 0
order_li = list(map(int,input().split())) # 명령받은 갯수

for order in order_li:
    order -=1 #남의 index는 3인데 값이 4로 들어오기 때문에 index맞추기 위해 -1
    r = r+dir[order][0]
    c = c+dir[order][1]
    if r<0 or r>=N or c<0 or c>=M: #벗어난다면 원상복구 시키고 continue
        r = r - dir[order][0]
        c = c - dir[order][1]
        continue
    tmp_idx_li = dice_idx[order]
    tmp_dice = copy.deepcopy(dice)
    for i in range(6):
        dice[i]=tmp_dice[tmp_idx_li[i]]
    if board[r][c]==0: #바닥면이 0인 경우
        board[r][c]=dice[5]
    else:
        dice[5]=board[r][c]
        board[r][c]=0
    print(dice[0])