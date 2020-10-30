#dfs
#0이 있으면 굳이 더 진행할 필요가 없다. 그래서 0이 아닐때만 진행하기
# 열 위치 체크하기

def dfs(cnt):
    global max_result,tmp_result
    if tmp_result<=max_result:
        return
    if cnt == N:
        if max_result<tmp_result:
            max_result= tmp_result
        return
    for i in range(N):
        if not visited[i]:
            if mapping[cnt][i]== 0:
                continue
            else:
                visited[i]=1
                tmp_result*=mapping[cnt][i]
                dfs(cnt+1)
                visited[i]=0
                tmp_result/=mapping[cnt][i]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping = [list(round(x*0.01,2) for x in map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    max_result = 0
    tmp_result = 1
    # print(mapping)
    dfs(0) # 배열의 행을 기준으로
    print(f'#{tc}',end=' ')
    print('%6f' %(max_result*100))
