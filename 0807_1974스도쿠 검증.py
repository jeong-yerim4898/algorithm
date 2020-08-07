T = int(input())
for test_case in range(1,T+1):
    sdoku = [list(map(int,input().split())) for _ in range(9)]
    row = 0
    colum = 0
    square =0
    answer = [0,1,1,1,1,1,1,1,1,1]

    #행열 확인
    for i in range(9):
        cnt_r_li = [0] * 10
        cnt_c_li = [0] * 10
        for j in range(9):
            cnt_r_li[sdoku[i][j]] +=1
            cnt_c_li[sdoku[j][i]] +=1
        if cnt_r_li == answer:
            row +=1
        if cnt_c_li == answer:
            colum +=1
    # 3x3 확인
    for i in range(0,9,3):
        for l in range(0,9,3):
            cnt_sq_li = [0]*10
            for j in range(i,i+3):
                for k in range(l,l+3):
                    cnt_sq_li[sdoku[j][k]] +=1
            if cnt_sq_li==answer:
                square +=1
    if row == colum and colum== square:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
