T = int(input())
for test_case in range(1,T+1):
    N , M = map(int,input().split())
    tool_li = [list(map(int,input().split())) for _ in range(N)]
    print(tool_li)
    max_pari = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_pari = 0
            for k in range(i,M+i):
                for m in range(j,M+j):
                    sum_pari+=tool_li[k][m]
            if sum_pari>max_pari:
                    max_pari = sum_pari
    print(f'#{test_case} {max_pari}')