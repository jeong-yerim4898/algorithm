n = int(input())
mapping=[[0]*n for _ in range(n)]
r=0
c=n//2
 #첫 숫자
for i in range(1,(n*n)+1):
    mapping[r][c]=i
    if i%n==0:
        r+=1
    else:
        r-=1
        c-=1
        if r<0:
            r=n-1
        if c<0:
            c=n-1
for i in range(n):
    for j in range(n):
        print(mapping[i][j],end=' ')
    print()
