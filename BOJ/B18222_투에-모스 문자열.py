
def getidx(N):
    v=1
    while v*2<N:
        v*=2
    return N-v
N = int(input())
cnt=0
while N!=0:
    cnt+=1
    N = getidx(N)
if cnt%2==1:
    print(0)
else:
    print(1)