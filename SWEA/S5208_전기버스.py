# 백트래킹 dfs
def dfs(idx):
    global tmp_result,min_result
    if idx >= N:
        if tmp_result<min_result:
            min_result=tmp_result
        return
    if min_result<=tmp_result:
        return
    start = idx
    possilbe = info[start]
    for i in range(start+possilbe,start,-1):
        tmp_result+=1
        dfs(i)
        tmp_result-=1

T = int(input())
for tc in range(1,T+1):
    info = list(map(int,input().split()))
    N = info[0]
    min_result = 98765432321
    tmp_result = 0
    dfs(1)
    print(f'#{tc} {min_result-1}')