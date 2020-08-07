T = int(input())
for test_case in range(1,T+1):
    cnt, total = map(int,input().split())
    A = [i for i in range(1,13)]
    N = len(A)
    eles = []
    for i in range(1<<N):
        ele=[]
        for j in range(N):
            if i&(1<<j):
                ele.append(A[j])
        eles.append(ele)
    cntt=0
    for i in range(len(eles)):
        ele_sum= 0
        for j in range(len(eles[i])):
            ele_sum+= eles[i][j]
        if len(eles[i]) ==cnt and ele_sum==total:
            cntt+=1
    print(f'#{test_case} {cntt}')