def black(selected,idx,cnt,tmp):
    global max_sum
    if cnt==3 and tmp<=M:
        if max_sum<=tmp:
            max_sum=tmp
        return
    if idx>=N:
        return
    selected[idx]=1
    black(selected,idx+1,cnt+1,tmp+cards[idx])
    selected[idx]=0
    black(selected,idx+1,cnt,tmp)

N,M= map(int,input().split())
cards = list(map(int,input().split()))
selected = [0]*N
cases=list()
max_sum=0
black(selected,0,0,0)
print(max_sum)