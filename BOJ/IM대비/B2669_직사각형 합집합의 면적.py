
board = [[0]*101 for _ in range(101)]
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            board[i][j]=1
cnt=0
for board_ele in board:
    for one in board_ele:
        if one:
            cnt+=1
print(cnt)