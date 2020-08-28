import sys
sys.setrecursionlimit(100000)

def grouping(x,y):
    check[x][y]=1
    delta_li = [(-1,0),(1,0),(0,-1),(0,1)]
    for delta in delta_li:
        gx,gy = x+delta[0],y+delta[1]
        if gx<0 or gx>=H or gy<0 or gy>=W:
            continue
        elif check[gx][gy]==0 and sheep[gx][gy]=='#':
            grouping(gx,gy)

T = int(input())

for test_case in range(1,T+1):
    H,W= map(int,input().split())
    sheep = [list(input().strip()) for _ in range(H)]
    check = [[0]*W for _ in range(H)]
    cnt=0
    for x in range(H):
        for y in range(W):
            if check[x][y]==0 and sheep[x][y]=='#':
                grouping(x,y)
                cnt+=1

    print(cnt)