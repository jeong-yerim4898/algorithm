#(0,0) 1,1 2,2 3,3 44 55 54 53
n = int(input())
mapping = [[0]*n for _ in range(n)]
x,y=-1,-1
count=0
for i in range(n):
    for j in range(i,n):
        if i%3==0:
            x+=1
            y+=1
        if i%3==1:
            y-=1
        if i%3==2:
            x-=1
        mapping[x][y]=count%10
        count+=1
for r in range(n):
    for c in range(r+1):
        print(mapping[r][c],end=' ')
    print()
