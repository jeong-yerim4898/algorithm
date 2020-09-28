
N = int(input()) # 색종이 갯수
board = [[0]*101 for _ in range(101)]
cnt = [0]*(N+1)
for k in range(1,N+1):
    paper = list(map(int,input().split()))
    for i in range(paper[0],paper[0]+paper[2]):
        for j in range(paper[1],paper[1]+paper[3]):
            board[i][j]=k

for m in board:
    for n in m:
        if n:
            cnt[n]+=1

for ans in cnt[1:]:
    print(ans)