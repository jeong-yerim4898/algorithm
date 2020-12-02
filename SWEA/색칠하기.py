T = int(input())
for test_case in range(1,T+1):
    size = [[0]*10 for _ in range(10)]
    sqs=[]
    square_cnt = int(input())

    for square in range(square_cnt):
        sqs.append(list(map(int,input().split())))
    for k in range(square_cnt):
        for i in range(sqs[k][0],sqs[k][2]+1):
            for j in range(sqs[k][1],sqs[k][3]+1):
                size[i][j] += sqs[k][4]

    cnt = 0
    for i in range(10):
        for j in range(10):
            if size[i][j]==3:
                cnt+=1
    print(f'#{test_case} {cnt}')