from math import sqrt
T = int(input())
for tc in range(1,T+1):
    start,end=map(int,input().split())
    dis = int(end-start)
    if dis<=3:
        print(dis)
    else:
        rule = int(sqrt(dis))
        if dis == rule**2:
            print(2*rule-1)
        elif rule**2<dis<=rule**2+rule:
            print(2*rule)
        else:
            print(2*rule+1)