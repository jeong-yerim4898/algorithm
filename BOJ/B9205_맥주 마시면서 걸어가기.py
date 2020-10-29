from collections import deque
import sys


def bfs(x,y):
    q= deque()
    co=list()
    q.append([x,y,20]) # +맥주
    co.append([x,y,20])
    while q:
        x,y,beer = q.popleft()
        if x== f1 and y ==f2:
            print('happy')
            return
        for nx,ny in con:
            if [nx,ny,20] not in co:
                dis = abs(nx-x)+abs(ny-y)
                if beer*50>=dis:
                    q.append([nx,ny,20])
                    co.append([nx,ny,20])
    print('sad')
    return

T = int(input())
for tc in range(1,T+1):
    num_con = int(input()) #convenience 편의점 수
    h1,h2 = map(int,input().split())
    con = [list(map(int,input().split())) for _ in range(num_con)]
    f1,f2 = map(int,input().split())
    con.append([f1,f2])

    bfs(h1,h2)

