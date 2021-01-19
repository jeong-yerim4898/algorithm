N=list(map(lambda x:int(x),list(input())))
N.sort(reverse=True)
for n in N:
    print(n,end='')