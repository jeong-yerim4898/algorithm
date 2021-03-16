def sero_omok(r,c,color):
    cnt=1
    checked = [(r,c)]
    sero_dir=[(-1,0),(1,0)]
    q=[(r,c)]
    while q:
        r,c =q.pop(0)
        for dir in sero_dir:
            nr = r + dir[0]
            nc = c + dir[1]
            if -1<nr<19 and -1<nc<19 and mapping[nr][nc]==color:
                if (nr,nc) not in checked:
                    cnt+=1
                    checked.append((nr,nc))
                    q.append((nr,nc))
    if cnt==5:
        return True
    else:
        return False

def garo_omok(r,c,color):
    cnt=1
    checked = [(r,c)]
    sero_dir=[(0,-1),(0,1)]
    q=[(r,c)]
    while q:
        r,c =q.pop(0)
        for dir in sero_dir:
            nr = r + dir[0]
            nc = c + dir[1]
            if -1<nr<19 and -1<nc<19 and mapping[nr][nc]==color:
                if (nr,nc) not in checked:
                    cnt+=1
                    checked.append((nr,nc))
                    q.append((nr,nc))
    if cnt==5:
        return True
    else:
        return False

def right_omok(r,c,color):
    cnt=1
    checked = [(r,c)]
    sero_dir=[(-1,1),(1,-1)]
    q=[(r,c)]
    while q:
        r,c =q.pop(0)
        for dir in sero_dir:
            nr = r + dir[0]
            nc = c + dir[1]
            if -1<nr<19 and -1<nc<19 and mapping[nr][nc]==color:
                if (nr,nc) not in checked:
                    cnt+=1
                    checked.append((nr,nc))
                    q.append((nr,nc))
    if cnt==5:
        return True
    else:
        return False
def left_omok(r,c,color):
    cnt=1
    checked = [(r,c)]
    sero_dir=[(-1,-1),(1,1)]
    q=[(r,c)]
    while q:
        r,c =q.pop(0)
        for dir in sero_dir:
            nr = r + dir[0]
            nc = c + dir[1]
            if -1<nr<19 and -1<nc<19 and mapping[nr][nc]==color:
                if (nr,nc) not in checked:
                    cnt+=1
                    checked.append((nr,nc))
                    q.append((nr,nc))
    if cnt==5:
        return True
    else:
        return False



T = int(input())
turn = [0]*T
for t in range(T):
    r,c = map(int,input().split())
    turn[t]=(r-1,c-1)
mapping= [[0]*19 for _ in range(19)]
for tc in range(T):
    color = (tc%2)+1
    mapping[turn[tc][0]][turn[tc][1]]=color
    if sero_omok(turn[tc][0],turn[tc][1],color) or garo_omok(turn[tc][0],turn[tc][1],color) or right_omok(turn[tc][0],turn[tc][1],color) or left_omok(turn[tc][0],turn[tc][1],color):
        print(tc+1)
        # print("오목")
        break
else:
    print(-1)
