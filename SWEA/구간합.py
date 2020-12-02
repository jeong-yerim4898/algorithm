T = int(input())
for test_case in range(1,T+1):
    num, space = list(map(int,input().split()))
    num_li = list(map(int,input().split()))

    box_sum = [0]*(num+1)
    for i in range(1,num+1):
        box_sum[i] = num_li[i-1]+box_sum[i-1]

    maxnum = minnum = box_sum[space]
    for i in range(space,num+1):
        if (box_sum[i] - box_sum[i-space])>maxnum:
            maxnum = box_sum[i] - box_sum[i-space]
        if (box_sum[i] - box_sum[i-space])<minnum:
            minnum = box_sum[i] - box_sum[i-space]

    print(f'#{test_case} {maxnum-minnum}')