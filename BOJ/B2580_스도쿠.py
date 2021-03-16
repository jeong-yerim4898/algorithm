def sdoku(idx):
    if idx == zero_cnt:
        for v in mapping:
            print(' '.join(map(str,v)))
        return
    r,c = zero_pos[idx]
    for i in range(1,10):
        if not row_arr[r][i] and not col_arr[c][i] and not box_arr[r//3*3+c//3][i]:
            row_arr[r][i], col_arr[c][i], box_arr[r // 3 * 3 + c // 3][i] =True,True,True
            mapping[r][c]=i
            sdoku(idx+1)
            row_arr[r][i], col_arr[c][i], box_arr[r // 3 * 3 + c // 3][i] =False,False,False
            mapping[r][c]=0

mapping = [list(map(int,input().split())) for _ in range(9)]
row_arr= [[False]*10 for _ in range(10)]
col_arr= [[False]*10 for _ in range(10)]
box_arr = [[False]*10 for _ in range(10)]

zero_pos=[] #0의 위치를 넣울 리스트
for r in range(9):
    for c in range(9):
        if not mapping[r][c]:
            zero_pos.append((r,c))
        else:
            row_arr[r][mapping[r][c]]=True
            col_arr[c][mapping[r][c]]=True
            box_arr[r//3*3+c//3][mapping[r][c]]=True
zero_cnt = len(zero_pos)
sdoku(0)