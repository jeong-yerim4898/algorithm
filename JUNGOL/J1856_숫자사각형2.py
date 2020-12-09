n,m = map(int,input().split()) # 높이,넓이
mapping = [[0]*m for _ in range(n)]
num = 0
for r in range(n):
    if r%2==0: #짝수 행
        for c in range(m):
            num+=1
            mapping[r][c]=num

    else:
        for c in range(m-1,-1,-1):
            num+=1
            mapping[r][c]=num
for r in range(n):
    for c in range(m):
        print(mapping[r][c],end=' ')
    print()