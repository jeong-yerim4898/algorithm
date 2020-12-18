def gcd_get(x,y):
    r = 0
    while y!=0:
        r=x%y
        x=y
        y=r
    return x
n = int(input())
a= list(map(int,input().split()))
gcd,lcm=a[0],a[0]
for i in range(1,n):
    gcd= gcd_get(gcd,a[i])
    lcm = lcm//gcd_get(lcm,a[i])*a[i]
print(gcd,lcm)

