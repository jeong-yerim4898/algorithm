
N,M = map(int,input().split())
meat = []
for _ in range(N):
    t1,t2 = map(int,input().split())  #무게 가격
    meat.append([t2,-t1]) # 가격,-무게
meat.sort() #가격 오름차순
meat.insert(0,[0,0])
# print(meat)
weight= 0
cost=0
flag =False
min_mum = 2147483647

for i in range(1,N+1):
    weight-=meat[i][1]
    if meat[i][0]==meat[i-1][0]:
        cost+=meat[i-1][0]
    else:
        cost=0
    if weight>=M:
        flag=True
        min_mum = min(min_mum,meat[i][0]+cost)

if flag:
    print(min_mum)
else:
    print(-1)