
board = [[0]*101 for _ in range(101)]
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    for dr in range(y,y+10):
        for dc in range(x,x+10):
            board[dr][dc]=1
ans=0
for k in board:
    for ele in k:
        if ele:
            ans+=1
print(ans)