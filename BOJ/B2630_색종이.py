def color_cnt(r,c,N):
    color = mapping[r][c]
    for i in range(r,r+N):
        for j in range(c,c+N):
            if mapping[i][j]!=color:
                return False
    return True


def dfs(r,c,N):
    global w_cnt,b_cnt
    if N==0:
        return
    if color_cnt(r,c,N):
        if mapping[r][c]==1:
            b_cnt+=1
        else:
            w_cnt+=1
    else:
        dfs(r,c,N//2)
        dfs(r+N//2,c,N//2)
        dfs(r,c+N//2,N//2)
        dfs(r+N//2,c+N//2,N//2)




N = int(input())
mapping = [list(map(int,input().split())) for _ in range(N)]

w_cnt=0
b_cnt=0
dfs(0,0,N)
print(w_cnt)
print(b_cnt)