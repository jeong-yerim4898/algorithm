
W,H = map(int,input().split())
N = int(input()) # 점선 갯수
w_li=[0,W]
h_li=[0,H]
w_max=0
h_max=0
for i in range(N):
    dir,point = map(int,input().split())
    if dir==0:
        h_li.append(point)
    else:
        w_li.append(point)
w_li.sort()
h_li.sort()
for i in range(len(w_li)-1):
    if w_max<w_li[i+1]-w_li[i]:
        w_max = w_li[i+1]-w_li[i]
for j in range(len(h_li)-1):
    if h_max<h_li[j+1]-h_li[j]:
        h_max=h_li[j+1]-h_li[j]
print(w_max*h_max)