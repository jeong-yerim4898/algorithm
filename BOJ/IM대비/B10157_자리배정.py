
C,R = map(int,input().split())
K = int(input())
board = [[0]*C for _ in range(R)]
cnt=C*R

dir_r = [1,0,-1,0]
dir_c = [0,1,0,-1]
r=0
c=0
d=0
num=1
if K>cnt:
    print(0)
else:
    while num<=cnt:
        if 0<=r<R and 0<=c<C and not board[r][c]:
            board[r][c]=num
            num+=1
        else:
            r-=dir_r[d]
            c-=dir_c[d]
            d=(d+1)%4
        r+=dir_r[d]
        c+=dir_c[d]

for i in range(R):
    for j in range(C):
        if board[i][j]==K:
            print(j+1,i+1)


