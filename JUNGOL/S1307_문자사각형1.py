n = int(input())
alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mapping = [[0]*n for _ in range(n)]
idx = 0
for c in range(n-1,-1,-1):
    for r in range(n-1,-1,-1):
        mapping[r][c]=alpabet[idx%26]
        idx+=1
for r in range(n):
    for c in range(n):
        print(mapping[r][c],end=' ')
    print()