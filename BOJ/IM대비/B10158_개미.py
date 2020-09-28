

w,h = map(int,input().split())
c,r = map(int,input().split())
time= int(input())
dc,dr = 1,1
for _ in range(time%(w*2)):
    if c==w or c==0:
        dc *=-1
    c+=dc

for _ in range(time%(h*2)):
    if r==h or r==0:
        dr *=-1
    r+=dr
print(c,r)
