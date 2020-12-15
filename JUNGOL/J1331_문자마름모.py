n = int(input())
alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mapping = [[0]*(2*n) for _ in range(2*n)]
dir_li=[(0,0),(1,-1),(1,1),(-1,1),(-1,-1)]

idx=0
size = n
for i in range(1,n+1):
    r=i
    c=n
    for j in range(1,5):
        for k in range(1,size):
            mapping[r][c]=alpabet[idx%26]
            idx+=1
            r +=dir_li[j][0]
            c+=dir_li[j][1]
    size-=1

mapping[n][n]=alpabet[idx%26]
# print(mapping)

left = n
right =n
for i in range(1,2*n):
    for j in range(1,left):
        print('  ',end='')
    for j in range(left,right+1):
        print(mapping[i][j],end=' ')
    if i<n:
        left-=1
        right+=1
    else:
        left+=1
        right-=1
    print()