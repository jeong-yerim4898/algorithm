from itertools import combinations

T = int(input())
for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    mappping=[list(map(int,input().split())) for _ in range(N)]

    cumul_sum=[[False]*(N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            tmp = mappping[i][j:j+M]
            tmp_ans = 0
            for tmp_len in range(1,1+M):
                for select in combinations(tmp,tmp_len):
                    if sum(select)<=C:
                        tmp_total = 0
                        for cell in select:
                            tmp_total+=cell**2
                        if tmp_total>tmp_ans:
                            tmp_ans=tmp_total
            cumul_sum[i][j]=tmp_ans
    print(cumul_sum)
    ans = 0
    for r in range(N):
        for c in range(N-M+1):
            sub_list = []
            sub_list+=cumul_sum[r][c+M:N-M+1]
            for y in range(r+1,N):
                sub_list+=cumul_sum[y]
            if sub_list:
                sub_ans=cumul_sum[r][c]+max(sub_list)
                if sub_ans>ans:
                    ans=sub_ans
    print(f'#{tc} {ans}')