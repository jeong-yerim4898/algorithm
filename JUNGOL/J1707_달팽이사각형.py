n = int(input())
num=1
dir_li = [(0,1),(1,0),(0,-1),(-1,0)] #오 아 왼 위
mapping = [[0]*n for _ in range(n)]
cnt = n*n
r=0
c=0
d=0
while num<=cnt:
    if -1<r<n and -1<c<n and not mapping[r][c]:
        mapping[r][c]=num
        num+=1
    else:
        r-=dir_li[d][0]
        c-=dir_li[d][1]
        d = (d+1)%4
    r+=dir_li[d][0]
    c+=dir_li[d][1]
for i in range(n):
    for j in range(n):
        print(mapping[i][j],end=' ')
    print()