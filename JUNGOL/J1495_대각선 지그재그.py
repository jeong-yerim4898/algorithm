n = int(input())
mapping = [[0]*(n*2) for _ in range(2*n)]

dir_li=[(1,-1),(-1,1)]
dir=0
num=1
r=1
c=1
for i in range(1,n+1):
    mapping[r][c]=num
    num+=1
    for j in range(1,i):
        r+=dir_li[dir][0]
        c+=dir_li[dir][1]
        mapping[r][c]=num
        num+=1
    if i%2==0:
        if i==n:
            r+=1
        else:
            c+=1
        dir=0
    else:
        if i==n:
            c+=1
        else:
            r+=1
        dir=1
for i in range(n-1,0,-1):
    mapping[r][c]=num
    num+=1
    for j in range(1,i):
        r += dir_li[dir][0]
        c += dir_li[dir][1]
        mapping[r][c] = num
        num += 1
    if i%2==0:
        r+=1
        dir=0
    else:
        c+=1
        dir=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(mapping[i][j],end=' ')
    print()