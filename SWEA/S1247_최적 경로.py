#dfs
def dfs(x,y):
    global min_result,tmp_result
    if 0 not in visited:
        tmp_result += abs(x-hx)+abs(y-hy)
        if tmp_result<=min_result:
            min_result=tmp_result
        tmp_result -= abs(x - hx) + abs(y - hy)
        return
    if tmp_result>=min_result:
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=1
            tmp_result+=abs(x-customer[i][0])+abs(y-customer[i][1])
            dfs(customer[i][0],customer[i][1])
            visited[i] = 0
            tmp_result -= (abs(x - customer[i][0]) + abs(y - customer[i][1]))

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #손님 숫자
    cx,cy,hx,hy,*info = list(map(int,input().split()))
    customer = list()
    for i in range(N):
        customer.append([info[i*2],info[i*2+1]])
    visited = [0]*N
    min_result = 987654321
    tmp_result = 0
    dfs(cx,cy)
    print(f'#{tc} {min_result}')
