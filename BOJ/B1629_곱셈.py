# 분할정복을 이용한 거듭제곱
def pow(a,b,c):
    if b==0:
        return 1
    n = pow(a,b//2,c)
    tmp = n*n%c
    if b%2==0:
        return tmp
    else:
        return a*tmp%c
A,B,C = map(int,input().split())
print(pow(A,B,C))

