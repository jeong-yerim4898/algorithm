def dfs(idx,sum_flavor,sum_kal):
    global ans
    if sum_kal>L:
        return
    if ans<sum_flavor:
        ans=sum_flavor
    if idx==N:
        return
    flavor,kal = ingredient[idx]
    dfs(idx+1,sum_flavor+flavor,sum_kal+kal)
    dfs(idx+1,sum_flavor,sum_kal)


T= int(input())
for tc in range(1,T+1):
    N, L = map(int,input().split())  # 재료 갯수, 총 칼로리
    ingredient = [list(map(int,input().split())) for _ in range(N)]
    ans=0
    dfs(0,0,0)
    print(f'#{tc} {ans}')