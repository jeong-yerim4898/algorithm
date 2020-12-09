n,m = map(int,input().split())
mapping = [[0]*n for _ in range(n)]
if m==1:
    num=1
    for r in range(n):
        for c in range(n):
            mapping[r][c]=num
        num+=1
if m==2:
    for r in range(n):
        num = 1
        if r%2==0: # 홀수
            for c in range(n):
                mapping[r][c]=num
                num+=1
        else:
            for c in range(n-1,-1,-1):
                mapping[r][c]=num
                num+=1
if m==3:
    for r in range(1,n+1):
        tmp = 1
        for c in range(1,n+1):
            if r ==1:
                mapping[r-1][c-1]=c
            if c == 1:
                mapping[r-1][c-1]=r
            if 1<r<n+1 and 1<c<n+1:
                tmp+=1
                mapping[r-1][c-1]=r*tmp
for r in range(n):
    for c in range(n):
        print(mapping[r][c],end=' ')
    print()