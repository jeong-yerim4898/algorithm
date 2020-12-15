n,m = map(int,input().split())
mapping = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if i==j or i==0:
            mapping[i][j]=1
        else:
            mapping[i][j] = mapping[i-1][j-1]+mapping[i-1][j]
if m==1:
    for i in range(n):
        for j in range(i+1):
            print(mapping[i][j],end=' ')
        print()
if m==2:
    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            print(' ',end='')
        for j in range(i+1):
            print(mapping[i][j],end=' ')
        print()
if m==3:
    for j in range(n-1,-1,-1):
        for i in range(n-1,j-1,-1):
            print(mapping[i][j],end=' ')
        print()
