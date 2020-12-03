
N,L,W,H = map(int,input().split())
end = max(max([W,H]),L)
start = 0

for i in range(10000):
    mid = (start+end)/2
    if (L//mid)*(W//mid)*(H//mid)>=N:
        start=mid
    else:
        end=mid

print('%.10f' %end)

