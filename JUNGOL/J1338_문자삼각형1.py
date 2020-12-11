n = int(input())
alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mapping=[[0]*n for _ in range(n)]
idx=0
for r in range(n):
    j=r
    for c in range(n-1,-1,-1):
        mapping[j][c]=alpabet[idx%26]
        idx+=1
        j+=1
        if j>n-1:
            break
for r in range(n):
    for c in range(n):
        if mapping[r][c]!=0:
            print(mapping[r][c],end=' ')
        else:
            print(' ',end=' ')
    print()