# time error
def isprime(n):
    if n<2:
        return False
    k=2
    for k in range(2,(n//k)+1):
        if n%k==0:
            return 0
    return 1

nums=list(map(int,input().split()))
for n in nums:
    if n<2:
        print('number one')
    elif isprime(n):
        print('prime number')
    else:
        print('composite number')
