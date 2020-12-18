n,m = map(int,input().split())
a,b = max(n,m), min(n,m)
mod =1
while mod>0:
    mod = a%b
    a,b = b,mod
print(a)
print(int(n*m//a))