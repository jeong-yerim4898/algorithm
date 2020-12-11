n,m = map(int,input().split())
if 0<n<101 and n%2!=0 and 0<m<5:
    if m==1:
        for r in range(n):
            if r<n//2+1:
                for j in range(r+1):
                    print('*',end='')
            else:
                for j in range(n-r):
                    print('*',end='')
            print()
    if m==2:
        for i in range(n//2):
            for j in range(n//2-i):
                print(' ',end='')
            for k in range(i+1):
                print('*',end='')
            print()
        for i in range(n//2+1):
            for j in range(i):
                print(' ',end='')
            for k in range(n//2-i,-1,-1):
                print('*',end='')
            print()
    if m==3:
        for i in range(n//2+1):
            for j in range(i):
                print(' ',end='')
            for k in range(n-(2*i)):
                print('*',end='')
            print()
        for i in range(n//2):
            for j in range(n//2-i-1):
                print(' ',end='')
            for k in range(i*2+3):
                print('*',end='')
            print()

    if m==4:
        for i in range(n//2+1):
            for j in range(i):
                print(' ',end='')
            for k in range(n//2+1-i):
                print('*',end='')
            print()
        for i in range(n // 2):
            for j in range(n//2):
                print(' ',end='')
            for k in range(i+2):
                print('*',end='')
            print()
else:
    print('INPUT ERROR!')