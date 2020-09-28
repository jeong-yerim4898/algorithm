

N,K = map(int,input().split())
room = [[0]*2 for _ in range(7)]
cnt = 0
for _ in range(N):
    S,Y = map(int,input().split())
    room[Y][S]+=1
    if room[Y][S]==K:
        cnt+=1
        room[Y][S]=0
for r in room[1:]:
    if r[0]!=0:
        cnt+=1
    if r[1]!=0:
        cnt+=1
print(cnt)