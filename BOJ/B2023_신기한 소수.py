def surprise(num):
    for n in range(2,int(int(num)**0.5)+1):
        if int(num)%n==0:
            return
    if len(num)==N:
        print(num)
        return
    for o in other:
        surprise(num+o)
N = int(input())
prime = ['2','3','5','7']
other = ['1','3','7','9']
for p in prime:
    surprise(p)