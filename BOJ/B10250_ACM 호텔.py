T = int(input())
for tc in range(1,T+1):
    H,W,N = map(int,input().split())
    Y = N%H
    X = N//H+1
    if Y==0:
        Y=H
        X-=1
    print(Y*100+X)