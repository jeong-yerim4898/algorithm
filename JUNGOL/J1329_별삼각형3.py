n = int(input())
if 0<n<101 and n%2!=0:
    for i in range(n//2):
        for j in range(i):
            print(' ',end='')
        for k in range((2*i)+1):
            print('*',end='')
        print()
    for i in range(n // 2+1):
        for j in range(n // 2-i):
            print(' ', end='')
        for k in range(n,i*2,-1):
            print('*', end='')
        print()
else:
    print('INPUT ERROR!')