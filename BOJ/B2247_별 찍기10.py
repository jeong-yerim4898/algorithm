def star(n):
    if n==3:
        mapping[0][:3]=mapping[2][:3]=[1]*3
        mapping[1][:3]=[1,0,1]
        return
    a=n//3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                mapping[a*i+k][a*j:a*(j+1)]=mapping[k][:a]
N = int(input())
mapping = [[0]*N for _ in range(N)]
star(N)
for i in mapping:
    for j in i:
        if j==1:
            print('*',end='')
        else:
            print(' ',end='')
    print()