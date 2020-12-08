while True:
    s,e = map(int,input().split())
    if s<2 or s>9 or e<2 or e>9:
        print('INPUT ERROR!')
    elif s>e:
        for n in range(1,10):
            for i in range(s,e-1,-1):
                if n*i<10:
                    print(str(i)+' * '+str(n)+' =  '+str(n*i),end='   ')
                else:
                    print(str(i)+' * '+str(n)+' = '+str(n*i),end='   ')
            print()
        break
    else:
        for n in range(1,10):
            for i in range(s,e+1):
                if n*i<10:
                    print(str(i)+' * '+str(n)+' =  '+str(n*i),end='   ')
                else:
                    print(str(i)+' * '+str(n)+' = '+str(n*i),end='   ')
            print()
        break

