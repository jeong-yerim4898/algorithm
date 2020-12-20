x,y= map(int,input().split())
s,e=0,1000000000
current = int(y*100/x)
if current>=99:
    print(-1)
else:
    while s<=e:
        mid = (s+e)//2
        nx=x+mid
        ny=y+mid
        if int(ny*100/nx)>current:
            e=mid-1
        else:
            s=mid+1
    print(e+1)
