# 최소하나 BFS? -> DFS + 백트래킹
# 기존의 보드를 바꾸는게 아니라 복사한 보드를 만들어 재귀함수를 진행해야한다.
# # 무조건 큰 색종이 부터 붙인다고 해결이 되지 않는다.
# 큰 색종이 부터 뭍이다가 애매하게 남아 완성하지 못 할 수도 있기 때문이다.
def dfs(n,s):
    global min_paper
    if s==0:
        if min_paper>n:
            min_paper=n
    elif n>=min_paper:
        return
    # elif sum(paper)==0:
    #     return
    else:
        for i in range(10):
            for j in range(10):
                if board[i][j]==1 and visited[i][j]==0:
                    # 왼쪽 모서리 시작점
                    for k in range(5,0,-1):
                        if paper[k]>0 and i+k<=10 and j+k<=10:
                            cover = 0
                            for r in range(i,i+k):
                                for c in range(j,j+k):
                                    # 방문하지 않았다면 cover가능하다.
                                    if visited[r][c]==0:
                                        cover+=board[r][c]
                            if cover==(k*k): # 커버 가능한 넓이가 색종이 넓이랑 같다면
                                for r in range(i,i+k):
                                    for c in range(j,j+k):
                                        visited[r][c]=1 # 해당 범위맡큼 방문했다고 표시
                                paper[k]-=1
                                dfs(n+1,s-(k*k))
                                for r in range(i,i+k):
                                    for c in range(j,j+k):
                                        visited[r][c]=0 # 해당 범위맡큼 방문했다고 표tl
                                paper[k]+=1
                    return

board = [list(map(int,input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
min_paper = 26 # 붙일수 있는 최소한의 종이
one_cnt = 0 # 1의 갯수
paper=[0,5,5,5,5,5] # 크기만큼 존재하는 색종이 갯수

for i in range(10):
    for j in range(10):
        if board[i][j]==1:
            one_cnt+=1

dfs(0,one_cnt) # 사용한 색종이 갯수 , 1의 갯수
if min_paper==26:
    min_paper=-1
print(min_paper)