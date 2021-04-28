'''
1. 국경선 열기 open_line
2. 인구이동 시작 move
'''
import sys

input = sys.stdin.readline
def open_li(r,c):
    global tmp_ans,line_cnt
    country_li.append((i, j))
    move_q=[]
    tmp_ans = 0
    q=list()
    q.append((r,c))
    while q:
        r,c = q.pop(0)
        move_q.append((r, c))
        tmp_ans += country[r][c]
        line_cnt += 1
        for dir in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr =r +dir[0]
            nc = c +dir[1]
            if -1<nc<N and -1<nr<N:
                if L<=abs(country[r][c]-country[nr][nc])<=R:
                    if (nr,nc) not in country_li:
                        country_li.append((nr,nc))
                        q.append((nr,nc))

    move(move_q)
    if line_cnt==1:
        return 0
    else:
        return 1

def move(move_q):
    average_move = tmp_ans//len(move_q)
    for coun in move_q:
        country[coun[0]][coun[1]]= average_move

N,L,R = map(int,input().split()) #크기, 범위
country = [list(map(int,input().split())) for _ in range(N)]
cnt=0
while True:
    country_li=[]
    line_cnt=0
    for i in range(N):
        for j in range(N):
            if (i,j) not in country_li:
                line_cnt+=open_li(i,j)
    if line_cnt==0:
        break
    cnt+=1
print(cnt)





