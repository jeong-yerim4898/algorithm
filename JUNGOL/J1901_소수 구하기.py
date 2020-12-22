# time error
def isprime(n):
    if n<2:
        return False
    k=2
    for k in range(2,(n//k)+1):
        if n%k==0:
            return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    if isprime(n):
        print(n)
        continue
    flag=0
    i=1
    while flag<1:
        if isprime(n-i):
            flag+=1
            print(n-i,end=' ')
            flag+=1
        if isprime(n+i):
            flag+=1
            print(n+i,end=' ')
        i+=1
    print()