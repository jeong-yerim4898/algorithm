n, m = map(int,input().split())

if 0<n<101 and 0<m<4:
    if m ==1:
        for r in range(n):
            for c in range(r+1):
               print('*',end='')
            print()
    elif m==2:
        for r in range(n):
            for c in range(n-1-r,-1,-1):
                print('*',end='')
            print()
    elif m==3:
        for i in range(1,n+1):
            for j in range(n-1,i-1,-1):
                print(' ',end='')
            for k in range(1,2*i):
                print('*',end='')
            print()
else:
    print('INPUT ERROR!')
