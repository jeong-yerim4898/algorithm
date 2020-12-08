s,e = map(int,input().split())

if s>e:
    for i in range(s,e-1,-1):
        k=0
        for n in range(1,10):
            if n * i < 10:
                print(str(i) + ' * ' + str(n) + ' =  ' + str(n * i), end='   ')
                k+=1
            else:
                print(str(i) + ' * ' + str(n) + ' = ' + str(n * i), end='   ')
                k+=1
            if not k%3:
                print()
        print()
else:
    for i in range(s,e+1):
        k = 0
        for n in range(1, 10):
            if n * i < 10:
                print(str(i) + ' * ' + str(n) + ' =  ' + str(n * i), end='   ')
                k += 1
            else:
                print(str(i) + ' * ' + str(n) + ' = ' + str(n * i), end='   ')
                k += 1
            if not k % 3:
                print()
        print()
