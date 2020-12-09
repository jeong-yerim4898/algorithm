n = int(input())
mapping = [[0]*n for _ in range(n)]
num=0
for c in range(n):
    for r in range(n):
        num+=1
        mapping[r][c]=num
for r in range(n):
    for c in range(n):
        print(mapping[r][c],end=' ')
    print()